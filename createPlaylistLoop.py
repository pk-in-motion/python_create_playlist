import dailymotion

d = dailymotion.Dailymotion()

d.set_grant_type(
    'password',
    api_key="...",
    api_secret="...",
    scope=['manage_playlists'],
    info={'username': "...", 'password': "...."}
    )

'''
count=0
while(count<3):

#url = d.upload('./examples/video.mp4')
    createPlay = d.post('/me/playlists', {
            'name': count,
            'description': 'test'
                    }
                )
count +=1
'''


for i in range(1, 5):
    #url = d.upload('./examples/video.mp4')
        createPlay = d.post('/me/playlists', {
                'name': 'playlist ' + str(i) + ' test',
                'description': 'test playlist' + str(i),
                'private': 'false'
                        }
                    )
        print (createPlay)

#video_id = (up['id'])
#print ("is done")
