# Submission Guide

Submissions to DrugMechDB have now been converted to a new Github Actions system
which allows for automated integration of pull requests.

#### Contents

1. [Prerequisites](#prerequisites)
    1. [Enable Github actions](#enable-github-actions)
    2. [Syncing your Fork](#syncing-your-fork)
2. [Submission](#submission)
    1. [Submitting new paths](#submitting-new-paths)
    2. [Claiming an indication group for curation](#claiming-an-indication-group-for-curation)
3. [Updates](#updates)
    1.  [Updating an existing path](#updating-an-existing-path)


## Prerequisites

### Enable Github Actions

The first thing that is required to use the new submission system is the enabling of Github Actions for your account.
You can do so by clicking the 'Actions' tab and choosing to enable Github Actions.


### Syncing your Fork

Keeping your fork up to date before submitting new paths is critical to ensuring that merge conflicts are minimized.
For this reason, we have implemented an action that automatically checks
for updates and creates pull requests to your account when they are found.
You can also trigger this manually to get the latest updates before making
a Pull Request.

### Manual Syncing using the Fork Sync action

#### Click the Actions Tab

![Actions](media/sync/1_actions.png)

This will bring you to the Github Actions page for this repository.

#### Click Sync Fork action

![Sync Fork](media/sync/2_sync_fork.png)

#### Click run workflow

![Run](media/sync/3_run.png)

After clicking `run workflow`, a confirmation box will come up, click to confirm.

#### Workflow Running

The workflow will appear with yellow coloring to signal that it is currently running.

![Running](media/sync/4_running.png)

#### New Pull Request

If differences are found, a new pull request will appear in the pull requests tab

![New Pull Request](media/sync/5_new_PR.png)


#### Merge the new request

Merge the new pull request to receive the changes.

![Merge](media/sync/6_merge.png)


## Submissions

### Claiming an indication group for curation

Please use the [issue template for claiming a group](https://github.com/SuLab/DrugMechDB/issues/new?assignees=&labels=upwork&template=indication-group-curation-claim.md&title=Curating+indication+group+)
to claim a group of indications so that other curators do not work on the same indications.

The `.zip` file containing the full set of grouped indications can be [downloaded here](
https://github.com/SuLab/DrugMechDB/raw/main/dmdb_indications_grouped.zip).

Before claiming, please ensure that the group you wish to claim has not been previously claimed or completed.
You can do this through searching the issues as shown in the image below.

![Search issues](media/new_claim/5_search_group.png)

The following steps outline the claiming process

#### 1. Go to the project's issues page
![Issues page](media/new_claim/1_issue_page.png)

#### 2. Select 'New Issue'
![New issue](media/new_claim/2_new_issue.png)

#### 3. Choose the 'Indication group curation claim' template and click 'Get started'
![Claim template](media/new_claim/3_claim_template.png)

#### 4. Please add the group number to end of the issue title
![Group Number](media/new_claim/4_group_number.png)

#### 5. Include the group number in the text as well
Feel free to replace the boilerplate text that appears in the template.
![Change Text](media/new_claim/6_change_text.png)

#### 6. Click 'Submit new issue'


### Submitting new paths.

New paths are to be submitted with the `submission.yaml` file. However, as this file will be constantly reset to
empty after every submission, it is **highly recommended** that you work in a separate file locally
while curating and only commit to this file once all changes are finished and ready to be submitted as a Pull Request.

The following guide will walk you through the steps for submitting new paths.

#### 1. Make edits to submission file and commit changes
![Submission File](media/submission/1_submission_file.png)

![Edit Sub File](media/submission/2_edit.png)
![Commit Changes](media/submission/3_commit.png)

Be sure and add a descriptive commit message.

#### 2. Submit a pull request
![Pull request](media/submission/4_pull_request.png)
![Create PR](media/submission/5_create.png)
![Submit PR](media/submission/6_description.png)

Again, please provide a description. If this submission corresponds to indications linked in one of the
issues, please provide either the issue number or the group number in the PR title.

#### 3. A pull request will now trigger Github actions Workflow

This workflow will test the file and integrate changes.
![Workflow is running](media/submission/6b_running.png)

Yellow text indicates the workflow is running.

Green Check mark means that the workflow is complete and successful.  If this happens you don't need to do
anything else.

![Workflow Complete](media/submission/9_Complete.png)

### Submission Error

If there are errors in the submission file, the workflow will fail. Errors need to be corrected an
the submission file should be re-submitted with a new Pull Request.

![Workflow Failure](media/submission/13_failure.png)

To determine why the check failed, click on the Details button on the right.  This will bring up Various Error Messages


##### Example Error 1

![Workflow Failure](media/submission/16_Path_error.png)

In this example, we see that one of our edge identifiers in the `'target_id'` position for the path
`cortisone acetate - Keratitis` is not present in the listed nodes.

##### Example Error 2

Here we have another error, this time the compiler cannot read the `submission.yaml` file. It describes what line
number is causing an error.

![Error Message](media/submission/14_error_message.png)

When we check the file, we see that the line has an identifier with an extra space within it, preventing the YAML
parser from correctly reading the file.

![Problem Line](media/submission/15_Line_number.png)


****

## Updates

### Updating an existing path

Similar to [submission](#submitting-new-paths), updates to existing paths are made via the `submission.yaml` file. As this
 `submission.yaml` file will be constantly reset to empty after every submission, it is **highly recommended** that you work in a
separate file locally while curating and copy or rename this file to `submission.yaml` when ready to commit
changes and submit a Pull Request.


#### Path Identifier

To perform an update, the `Path ID` must be included in the `submission.yaml` file for hte path that is to be updated.
The value of a `Path ID` is automatically generated with the submission of each new path, and can be found on the path's
webpage.

![Path Identifier](media/update_records/1_path_id.png)


The identifier for the path should be included as an `_id` field under the `graph` field in the submission. See the (truncated)
example below of the path pictured above for the precise location of the `_id` field.


    -   directed: true
        graph:
            _id: DB00704_MESH_D000437_1
            disease: Alcoholism
            disease_mesh: MESH:D000437
            drug: Naltrexone
            drug_mesh: MESH:D009270
            drugbank: DB:DB00704
        links:
        -   key: decreases activity of
            source: MESH:D009270
            target: UniProt:P41145
        -   key: molecularly interacts with
            source: UniProt:P41145
            target: UniProt:P01213
        -   key: positively correlated with
            source: UniProt:P01213
            target: HP:0030858
    ...
        
#### Update details

The update process is similar to the [submission](#submitting-new-paths) process, performing the same validation checks and
producing the same error when a problem. If unfamiliar with this process, please see the detailed section above.

Updates may be performed as a batch (multiple updates simultaneously) however, they may not be performed at the same time
as submission of new paths. Those must be included in a separate Pull Request. Adding new paths at the same time as updating
existing paths will produce an error.

