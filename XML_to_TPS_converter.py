#Convert XML outputs from ML-Morph into the format used by TPS tools
#must be run within the directory containing the file

import re

#Setup steps:

XMLFilename = input("XML Filename?")

OutputFile = input("TPS output filename?")
newfilename = str(OutputFile)

ImageHeight = int(input("Image height in pixels? No answer defaults to 2848").strip() or 2848)

data = []


#Read in the XML:
with open(XMLFilename) as f:
    data = f.read().split("<")


#counter for fish ID as used in TPS files
id = 0 

#empty string to hold image names extracted from XML
imageName = "" 

#List to store lists of coordinates
coords = []

#Dictionary to store image name plus lists of landmark coordinates
newfile = {}

for line in data:

    if line[:10] == "image file":
        imageName = re.search("IMG.*JPG", line).group() #Extract image name

    if line[:9] == "part name": #The XML files denote each individual landmark as a "part"
        xcoord = str(re.search("x=\"[0-9]*", line).group().split("\"")[1] + ".00000") #Not sure why, but TPS coordinates have a 'precision' of 5 decimal places
        ycoord = str(str(ImageHeight - int(re.search("y=\"[0-9]*", line).group().split("\"")[1])) + ".00000") #TPS files use inverted Y coordinates
        xy = [xcoord, ycoord]
        coords.append(xy)

    if line[:4] == "/box": #The XML file "box" is the area in which the ML algorithm has detected an object (fish)
        newfile[imageName] = coords.copy()

    if line[:7] == "/image>":
        coords.clear()
        

    if line[:7] == "/images":  #End of the xml file
        with open(newfilename, "a") as f:

            for image in newfile: #write the TPS file line by line

                f.write("LM=" + str(len(newfile[image])) + "\n") #number of landmarks

                for coordinates in newfile[image]: #read the dictonary entry for the image ID
                    f.write(str(coordinates[0]) + " " + str(coordinates[1]) + "\n") #Put in the x and y coordinates for each landmark sequentially

                f.write("IMAGE=" + str(image) + "\n") #write the image name

                f.write("ID=" + str(id) + "\n") #identify the sequential location of the image

                id += 1