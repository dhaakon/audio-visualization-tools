import echonest.remix.audio as audio

class SongAnalyzer:
    def __init__( self, mp3 ):
        self.mp3 = mp3
        self.audio_file = audio.LocalAudioFile(self.mp3)
        self.analysis = self.audio_file.analysis
        self.beats = self.analysis.beats
        self.beats.reverse()

        #print self.audio_file.analysis.id
        print audio
        audio.getpieces( self.audio_file, self.beats ).encode("remix.mp3")
