# Test Code here....

from resume_parser.utils import *
from spacy.matcher import Matcher
from tqdm import tqdm
import glob


# parent_dir = os.getcwd() 
# print(parent_dir)


if __name__ == "__main__":

    nlp = spacy.load('en_core_web_sm')    # check the model..............
    matcher=Matcher(nlp.vocab)

    # folderpath= r'resume_parser/mediafiles'
    # filelist = glob.glob(folderpath +"\\*.txt")  # textfile here only...

    folderpath=r'resume_parser/mediafiles/resumes'
    filelist = glob.glob(folderpath +"\\*.*")  # All Typres of files.....

    print(filelist)
    for file in tqdm(filelist,disable=False):
        text=extract_text(file,'.'+file.split('.')[-1])

        name=extract_name(nlp(text),matcher)
        print(name)






