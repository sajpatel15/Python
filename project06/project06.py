''' Module Project06.py'''
'''
Author: Saj Patel
Purpose: To interact with an API and read data, filter it an provitd an approprate
        output
Date: 8/15/2020
'''
import requests, json, time

def get_top_5_comments(imgur_username):
    
    comments  = []

    # looping though all the pages 
    for num in range(100):
        # storing the url for the website that includes the page number
        url = 'http://imgur.com/user/' + imgur_username + '/index/newest/page/' + str(num) + '/hit.json?scrolling'

        # generating a request to get the url
        r = requests.get(url)

        # ensuring that there was a sucesfull connection
        if r.status_code == 404:
            print('Not found')
            return
        elif r.status_code == 200:
            
            # checking to see if the data is empty cause that would mean the page is empty which means we dont need to loop through anymore
            if r.text == '':
                break
            else:
                # getting the data from the site and storing it in python format
                data = r.json()['data']['captions']['data']

                comments.extend(data)

    # sorting the data in ascending order of points
    sorted_by_key = sorted(comments, key = lambda d: d['points'])

    # creating a new list where the final comments will be stored
    top_5_comments = []

    # filtering the data so that the new list of dictionaries only have the requried data
    for num in range(1,6):
        new_dict = dict()
        for (key, value) in sorted_by_key[0-num].items():
                # check for hash
                if key == 'hash':
                    new_dict[key] = value

                # check for title
                elif key == 'title':
                    new_dict[key] = value

                # check for points
                elif key == 'points':
                    new_dict[key] = value

                # check for date
                elif key == 'datetime':
                    new_dict[key] = value

        # appending the dictionary of filtered data to the comments lists
        top_5_comments.append(new_dict)

    # printing the comments appropriately
    for num in range(0,5):
        comment_num = str(num+1) + '.'
        print(comment_num, str(top_5_comments[num].get('hash')))
        print("Points:", str(top_5_comments[num].get('points')))
        print("Title:", str(top_5_comments[num].get('title')))
        print("Date:", top_5_comments[num].get('datetime'),'\n')
        



if __name__ == '__main__':

    username = input('Enter username: ')
    get_top_5_comments(username)

