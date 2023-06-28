import os as _os
import pathlib as _pl
import ftplib as _ftplib
import urllib as _urllib
import pickle as _pickle
import requests as _requests
import datetime as _datetime

__all__ = ['get_content_type', 'is_downloadable', 'is_text', 'download_file', 'save_text',
            'is_ftp', 'download_ftp', 'download', 'load_api_results']


def get_content_type(url):
    """Determines the content type of a URL"""
    h = _requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    return content_type


def is_downloadable(url):
    """Determines if URL is a downloadable resource"""
    content_type = get_content_type(url)
    if is_text(url, content_type):
        return False
    if 'html' in content_type.lower():
        return False
    return True


def is_text(url, content_type=None):
    """Determines if a URL points to text"""
    # Allow user to skip step if content type already retrevied
    if content_type is None:
        content_type = get_content_type(url)
    # some text files have no content type header
    if content_type is None or "text" in content_type:
        return True
    return False


def download_file(url, out_name):
    """Downloads a file ot the given out_name"""
    r = _requests.get(url, allow_redirects=True)
    open(out_name, 'wb').write(r.content)


def save_text(url, out_name):
    """Save text to given filename to out_name"""
    r = _requests.get(url)
    open(out_name, 'w').write(r.text)


def is_ftp(url):
    """Determine if a url is over ftp protocol"""
    return _urllib.parse.urlparse(url).scheme == 'ftp'


def download_ftp(url, out_name):
    """Download a file from an ftp server to out_name"""
    # Parse the FTP url
    parsed = _urllib.parse.urlparse(url)
    server = parsed.netloc
    dl_path = parsed.path

    # Download the file
    ftp = _ftplib.FTP(server)
    ftp.login()
    ftp.retrbinary("RETR {}".format(dl_path), open(out_name, 'wb').write)
    ftp.quit()

def download(url, out_name=None, redownload=False):
    """
    Determiens the proper protocol to download a file from a URL.
    Will save the file to `out_name` and will by default skip if the output
    file already exists.

    :param url: The URL of the file to download
    :param out_name: The location to save the file to. If None, will parse the URL and save to cwd.
    :param redownload: Boolean, if False, will not download the file if `out_name` already exists.
        If True, will download the file again even if it exists.

    :return: None
    """

    if out_name is None:
        # Take the final element of the URL as filename if no out_name passed.
        out_name = url.split('/')[-1]
        file_name = out_name
    else:
        #Grab the base filename
        file_name = _os.path.basename(out_name)
        # use the url filname in case only a directory (ending in /) is passed
        if file_name == '':
            file_name = url.split('/')[-1]
        # Make sure the output directory exists
        out_dir = _os.path.dirname(out_name)
        if not _os.path.exists(out_dir):
            _os.path.makedirs(out_dir, exist_ok=True)

    # Only redownload an already existing file if user explicitly states
    if _os.path.exists(out_name) and not redownload:
        print('File {} exits. Skipping...'.format(file_name))
        return None

    # Use FTP for ftp transfers
    if is_ftp(url):
        print('Getting {} from ftp server'.format(file_name))
        download_ftp(url, out_name)
        print('Done')
    # Download downloadable files
    elif is_downloadable(url):
        print('Downloading {}'.format(file_name))
        download_file(url, out_name)
        print('Done')
    # Save text
    elif is_text(url):
        print('Saving {}'.format(file_name))
        save_text(url, out_name)
        print('Done')
    # Skip non-conforming files and print to screen.
    else:
        print(file_name, ": Not a downloadable file or text... ")
        print('Skipping....')


def load_api_results(res_file_name, re_scrape=False, scrape_function=lambda **f: None, **kwargs):
    """
    Wrapper for API scraping functions. Loads results from an api query if on disk. If file does not exit,
    or rescrape is true, and an api function is passed, the API will be rescraped for data.

    :param res_file_name: string or Path, the filename to load or save to (must be .pkl for now).
        If `{}` is included in the filename, will glob on that point in the filename and take the highest value
        (newest if that happpens to correspond to a date). Also, if a download is performed and the file is saved,
        a `{}` will be filled with the current date in the output file name.
    :param rescrape: bool, re-download the data even if a file matching the input name already exists.
    :param scrape_function: the function to be called if the datafile does not exist, or if re_scrape is true.
    :param **kwargs: any keyword arguments for the scrape funtion.

    :return: Data either loaded from disk or scraped from an api.
    """
    # Make sure filname is string
    if not isinstance(res_file_name, _pl.Path):
        res_file_path = _pl.Path(res_file_name).resolve()
    else:
        res_file_path = res_file_name.resolve()
        res_file_name = str(res_file_path)

    # Ensure we have a formatting characters so we can glob to load and save with date
    if '{}' not in res_file_path.name:
        # record the parent directory
        parent_path = res_file_path.parent

        # add a formatting char before the first .
        n_spl = res_file_path.name.split('.')
        new_name = n_spl[0] + '_{}.' + '.'.join(n_spl[1:])

        # rebuild the path and file names
        res_file_path = _pl.Path(parent_path).joinpath(new_name)
        res_file_name = str(res_file_path)

    # Glob for dump files and if there are more than one, take the most recent
    dump_files = list(res_file_path.parent.glob(res_file_path.name.format('*')))
    if len(dump_files) < 1 or re_scrape:
        # Scrape (or re-scrape) the  API and save
        res = scrape_function(**kwargs)

        if res:
            with open(res_file_name.format(_datetime.datetime.now().strftime("%Y-%m-%d")), 'wb') as f_out:
                _pickle.dump(res, f_out)
    else:
        # Load the most recent previously saved dump
        dump_file = sorted(dump_files, reverse=True)[0]
        res = _pickle.load(open(dump_file, 'rb'))
    return  res

