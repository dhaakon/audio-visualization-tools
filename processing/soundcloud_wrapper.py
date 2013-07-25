import soundcloud
import song_analyzer

class soundcloudWrapper:

    def __init__ ( self ):

        #Establish the client
        self.client = soundcloud.Client( client_id=SOUNDCLOUD_CLIENT_ID )

    def getTrackById ( self, trackId ):

        # Grab the track
        self.track = self.client.get( trackId )
        
        self.user  = self.track.user[ 'username' ]
        self.title = self.track.title

        # Grab the URL
        self.track_url = self.client.get( self.track.stream_url, allow_redirects=False )

# Taken from http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
import urllib2

class FileRetriever:
    def __init__ (self, url, artist, title):
        self.url      = url
        self.fileName = str(artist + '-' + title + '.mp3').replace(' ', '')

        print self.url

        self.request  = urllib2.urlopen( self.url )
        self.file     = open( self.fileName, 'wb' )
        self.meta     = self.request.info()
        self.fileSize = int( self.meta.getheaders('Content-Length')[0] )

        self.downloadedBytes = 0
        self.blockSize       = 8192

        print "Downloading: %s Bytes: %s" % ( self.fileName, self.fileSize )

        while True:
            buffer = self.request.read( self.blockSize )
            if not buffer:
                break

            self.downloadedBytes += len( buffer )
            self.file.write( buffer )
            self.status = r"%10d  [%3.2f%%]" % ( self.downloadedBytes, self.downloadedBytes * 100. / self.fileSize )
            self.status = self.status + chr(8) * ( len( self.status ) +1 )
            print self.status,

        self.file.close()

        song_analyzer.SongAnalyzer( self.fileName )

s = soundcloudWrapper()
s.getTrackById( 'tracks/8771103' )

f = FileRetriever( s.track_url.location, 
                   s.user, 
                   s.title )
