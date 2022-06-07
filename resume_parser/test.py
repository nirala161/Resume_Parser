# Test Code here....

from resume_parser.utils import *
from spacy.matcher import Matcher
from tqdm import tqdm
import glob
import sys, os
# parent_dir = os.getcwd() # find the path to module a
# # Then go up one level to the common parent directory
# path = os.path.dirname(parent_dir)
# # Add the parent to sys.pah

sys.path.append(r'C:\Users\niral\Desktop\Resume_Parser')


if __name__ == "__main__":

    nlp = spacy.load('en_core_web_trf')    # check the model..............
    matcher=Matcher(nlp.vocab)

    # folderpath= r'resume_parser/mediafiles'
    # filelist = glob.glob(folderpath +"\\*.txt")  # textfile here only...

    folderpath=r'resume_parser/mediafiles/resumes'
    filelist = glob.glob(folderpath +"\\*.*")  # All Typres of files.....

    print(filelist)
    result={}
    
    for file in tqdm(filelist,disable=False):
        text=extract_text(file,'.'+file.split('.')[-1])
        nlp_text=nlp(text)
        result['name']=extract_name(nlp_text,matcher)
        result['education']=extract_education(text)
        result['organisation_name']=extract_organisations_name(nlp_text)
        print(result)






