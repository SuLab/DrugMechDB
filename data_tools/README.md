# Data Tools

A collection of random tools for manipulating data,
with the primary goal of producing hetnets.

## Description

### Overview

This is a collection of functions and tools for manipulating data. 

### Motivation

This project was built from common operations I run in python and pandas. As I started to notice I was reusing blocks of
code throughout my various projects I decided to abstract them into functions, and packge them in a way they could be
easily integrated into future projects. For a project that uses this 
toolset see [metapaths](https://github.com/mmayers12/metapaths/).

### Features

This repo contains tools for:

- Downloading data
- Reshaping Series and DataFrames
- Managing Graphs as DataFrames (separate Nodes and Edges objects)
- Some prebaked Seaborn plots with a particular style
- Processing and plotting Machine Learning results

### Re-use and contributions statement

Feel free to reuse code as you see fit.  If you would like to make changes to the code, feel free to 
build your own forked version.


## Getting Started

To install the latest version with pip use the following command:

    pip install git+https://github.com/mmayers12/data_tools

### Requirements 

See setup.py for a list of requirements.

## Usage

### How to use

To use functions in this library import them into your script.

### Code examples

    from data_tools.graphs import combine_nodes_and_edges
    combo = combine_nodes_and_edges(nodes, edges)

## Project Status

### Current status / build / version

Project is currently under heavy development. Methods and features are subject to change greatly on subsequent versions.

Current version is 0.0.8.

## Credits

### Contact info

For bug reports please email mmayers[at]scripps.edu or raise an issue on Github.

