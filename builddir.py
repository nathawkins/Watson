"""
Function + command line utility for creating a new directory in the Watson parent directory
for a new textbook or piece of content.
"""
# Imports --------------------------------------------------------------------------
import os
import re

from argparse import ArgumentParser

# Functions ------------------------------------------------------------------------
def constructCommandLineArguments():
    '''
    Constructs parser for command line arguments. All command line arguments
    should be entered with "" to allow for multiword strings to be parsed.

    Parameters
    ----------
    None
    
    Returns
    -------
    ArgumentParser() with command line inputs for author, title, and description.
    '''
    # Initialize
    parser = ArgumentParser()

    # Add arguments
    ## Author
    parser.add_argument("-a", "--author", help = "Name of Author", required = True)

    ## Title
    parser.add_argument("-t", "--title", help = "Title of Textbook or Material", required = True)

    ## Brief description
    parser.add_argument("-d", "--description", help = "Short Description of Material", required = True)

    return parser


def initializeChildDirectory(author, title, description):
    '''
    Create child directory from inputs and populate directory with
    short, template README.md file.

    Parameters
    ----------
    author:
        str. Name of author
    title:
        str. Title of textbook or reference material
    description:
        str. Brief description of the reference material

    Returns
    -------
        None. Generates directory and populates template directory if successful.
    '''
    # Get author last name
    author_last_name = author.split(" ")[1].lower()

    # Create a path-safe short designation from the title
    short_title = re.sub(r'\W+', '', title[:10]).lower()

    # Create directory name
    directory_name = f'{short_title}_{author_last_name}'

    # Create a new directory with the directory name
    directory = os.path.join(os.getcwd(), directory_name)
    os.makedirs(directory, exist_ok = True) # exist_ok prevents error if dir exists

    # Create template README.md file in new directory
    with open(os.path.join(directory, 'README.md'), 'w') as f:
        f.write(f'# {title}\n\n')
        f.write(f"Author: {author}\n")
        f.write(f"Description: {description}\n\n")
        f.write(f"# Contents\n")


# Main -----------------------------------------------------------------------------
def main():
    # Create command line arguments
    parser = constructCommandLineArguments()

    # Parse arguments for input values
    args = parser.parse_args()

    # Create directory
    initializeChildDirectory(args.author, args.title, args.description)

    return 0


if __name__ == '__main__':
    main()