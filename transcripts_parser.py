#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
23 November 2017
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Parsing the conversation transcripts with annotations

Annotation template: message_type>speaker_turn>message
e.g. greeting>E>Hi?

'''
import os

SAMPLE_TRANSCRIPT_FILE = 'data_gv_at/transcript1_1.txt'
# SAMPLE_TRANSCRIPT_FILE = 'opendataportal_at/transcript13_2.txt'

OPERATIONS = ['greeting()', 'set(keywords)', 'prompt(keywords)',
              'list(keywords)', 'success()', 'link(dataset)',
              'bool(data)', 'question(data)', 'top(keywords)', 'count(data)',
              'verify()', 'reject()', 'confirm()', 'prompt(link)', 'more()']


def parse_transcript(transcript_file):
    with open(transcript_file) as file:
        for line in file:
            try:
                intent, turn, message = line.split('>')
                # show the process template
                print turn, intent
                
                if intent not in OPERATIONS:
                   print("Unknown intent" + intent)
            except:
                if '>' in line:
                    print("Error parsing line:")
                    print line


def test_parse_transcript():
    parse_transcript(SAMPLE_TRANSCRIPT_FILE)


def parse_all_transcripts(dirs =['data_gv_at', 'opendataportal_at']):
    for portal_dir in dirs:
        for file in os.listdir(portal_dir):
          if file[-4:] == '.txt':
            # print file
            parse_transcript('/'.join([portal_dir, file]))
            print '\n'


def main():
    parse_all_transcripts()


if __name__ == '__main__':
    main()
