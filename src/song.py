import re
import json
from flask import jsonify
from props import bcolors, count_lines_endings

class Song:
    """
    object handling exporting song \n
    here will be done every formating and preparation for final export
    """

    def __init__(self, songText, songName, params):
        """constructor

        Args:
            songText (string): plain text of the song
            songName (string): name of the song
            params (array): all params set or with default value
        """
        self.songText = songText # load text of song
        self.songName = songName # song name
        self.params = params # params defining the requirements for the output

    def __putSongInOrder(self):
        """it takes the song plain text and according to the param of song-format puts
        the verses into the right order
        """
        
        # split all verses, bridges and chorus in the song according to their signs
        songTextInParts = re.split("[0-9]+[:.]|[R][:.]|[C][:.]|[B][:.]", self.songText)
        songTextInParts.pop(0) # pop the first blank space in array
        # get the verses numbers from the lyrics, so the verses above could be find
        versesNumbers = re.findall("[0-9]+[:.]|[R][:.]|[C][:.]|[B][:.]", self.songText)
        
        buildedSong = [] # here will be builded the song parts in the right order

        if self.params['songformat'] == 0 :
            # it should be only in its default variant
            for verseSign in versesNumbers: # find the desired part in existing parts found in song
                    verseIndex = versesNumbers.index(verseSign)
                    buildedSong.append([verseSign, songTextInParts[verseIndex].strip()])      
        else:
            # song has its defined format 
            # go through the string representing the desired song format (i.e. verses order)
            for part in self.params['songformat']:
                try:
                    for i in versesNumbers: # find the desired part in existing parts found in song
                        if part in i : # if the sign of the verse is found, then add the verse to the final song form
                            verseSign = i
                            verseIndex = versesNumbers.index(verseSign)
                            buildedSong.append([verseSign, songTextInParts[verseIndex].strip()])
                            break         
                except Exception as e:
                    print(str(e)) # print into the terminal if any exception occurs

        # load the builded song into the variable for the final representation
        return buildedSong
    
    def __buildSlidesFromBuildedSong(self, buildedSongArray):
        # TODO these three params have to be passed here in variable 'params'
        max_lines = 5 # TODO probably count count max lines from desired font size
        min_lines = 2 

        # here will be stored the slides in json one by one
        slides = []

        # first slide build
        slides.append({            
            "title" : self.songName,
            "sub-title" : self.params['songnumber']
        })

        # other slides lyrics build
        for verse in buildedSongArray:
            # line count check
            num_of_lines = count_lines_endings(verse[1])
            if num_of_lines > max_lines:
                # then divide the lines into two or more slides                
                current_slide_verse = verse[0] + ".: "
                currently_written_lines_on_slide = 0
                # read currently proccessed verse line by line
                for line in str(verse[1]).splitlines():
                    currently_written_lines_on_slide += 1 # count up the current line
                    if currently_written_lines_on_slide <= max_lines:
                        current_slide_verse += line.strip() + "\n"
                    else:
                        # write out current slide
                        slides.append({
                            "content" : current_slide_verse
                        })
                        # reset counter of lines for current slide
                        currently_written_lines_on_slide = 1
                        # write currently processed verse line to the
                        current_slide_verse = line.strip() + "\n"

                # in case the last slide hasn't been written
                if currently_written_lines_on_slide != 0:
                    # write out current slide
                    slides.append({
                        "content" : current_slide_verse
                    })
            else:
                # otherwise just create new slide with the text
                slides.append({
                    "content" : verse[1]
                })
            
        return slides

    def __buildRawPdf(self, buildedSongArray):
        ()

    def exportJson(self) :
        """method generating json file with text and display options

        Returns:
            string : file name with its extension
        """
        
        # get the verses in order - in array with doubles verseSign-verseText
        buildedSongArray = self.__putSongInOrder()
        
        # build slides from builded song text
        # TODO place for decision whether to create raw pdf or presentation
        if (self.params['fileformat'] in ['ppt', 'pdf']):
            slides = self.__buildSlidesFromBuildedSong(buildedSongArray)
        else: # rawpdf
            slides = self.__buildRawPdf(buildedSongArray)

        #create json model
        song_data = { 
            "file" : {
                "name" : self.songName,
                "num-of-slides" : len(slides),
                "export-format" : self.params['fileformat'],
            },
            "display-options" : {
                "font-family" : self.params['fontfamily'],
                'font-size' : self.params['fontsize'],
                "background" : self.params['background']
            },
            "slides" : slides
        }
        
        # return json data
        return song_data
