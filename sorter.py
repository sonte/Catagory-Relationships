from xml.dom import minidom
import xml.etree.ElementTree as et

__author__ = 'sonte'
# creating our dictionaries
relationDictionary = dict()
catDictionary = dict()
#pulling in the xml and getting all the trees with the attribute 'category'
doc = et.parse('categories.xml')
child = doc.findall('category')
x = 0
'''
Under the Category tree in the xml assigning the text from the id to be the key
and the name to be the value in the catDictionary
'''
while (x < len(child)):
    catDictionary[int(child[x][0].text)] = child[x][1].text
    x = x + 1

#Parsing the xml from the other xml file and getting all the trees with the attribute 'category_relationship'
doc = et.parse('category_relationships.xml')
child = doc.findall('category_relationship')
x = 0
'''
#Under the 'category_relationship' tree first we check if the parent_id already exists.  If it does we append
#the child_id to the existing key in the dictionary.  If it does not, we create a new key with the parent_id and
#child_id as the value.
'''
while (x < len(child)):
    if int(child[x][0].text) in relationDictionary.keys():
        relationDictionary[int(child[x][0].text)].append(int(child[x][1].text))
    else:
        relationDictionary[int(child[x][0].text)] = [int(child[x][1].text)]
    x = x + 1
x = 0
#This goes through all of the keys in the relationDictionary.
for key in relationDictionary:
    first = ''
    second = ''
    '''
    First it checks to make sure that the key's value does not have multiple entries.  If it does we know that
    it is not going to be our starting point, so skip to the next key.
    '''
    if (len(relationDictionary[key]) == 1):
        '''
        Here is checks to make sure that the parent object is not a child object.  If the parent object is a child
        object it will ignore it and move on the the next parent object.
        '''
        findkey = relationDictionary.get(key)
        list = relationDictionary.get(findkey[0])
        if key not in list:
            '''
            Next it checks to make sure that the key's value exists in the catDictionary.  If it does not, then there
            is no corresponding name in the categories.xml files and should be skipped.
            '''
            if (catDictionary.get(key) != None ):
                #Now that we have gotten to this point, we know that the key is the first word in the catDictionary.
                first = catDictionary.get(key)
                '''
                We know that they value of the key is the second word, but this is a list so we have to pull it out to convert it
                because none of the keys are lists in catDictionary. list[0] is just and int which is what the keys are in
                catDictionary
                '''
                list = relationDictionary.get(key)
                second = catDictionary.get(list[0])
                '''
                We know that the second word is going to be followed by the third and final word.  We use the second word as the key and
                get its list of values and the different possible third words.
                '''
                list = relationDictionary.get(list[0])
                #go through all of the items in list to get all of the possible third word combinations.
                for items in list:
                    #check to make the third word exits of course.
                    if (catDictionary.get(items) != None):
                        third = catDictionary.get(items)
                        print(first + " > " + second + " > " + third)
    x = x + 1




