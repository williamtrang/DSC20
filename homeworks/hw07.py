"""
DSC 20 Homework 07
Name: William Trang
PID:  A16679845
"""

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with 1220980 streams
    >>> track1.get_artist()
    'Cordae'

    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'

    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True

    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False

    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']

    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759

    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA

    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799

    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'

    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'


    # Add your doctests below here #
    >>> t1 = Song('TT', 3, 'Twicecoaster: Lane 1', 'TWICE', 6000000)
    >>> t1.get_name()
    'TT'

    >>> t1.get_length()
    3

    >>> t1.get_album()
    'Twicecoaster: Lane 1'

    >>> t1.get_artist()
    'TWICE'

    >>> t1.get_streams()
    6000000

    >>> print(t1)
    'TT' by TWICE on 'Twicecoaster: Lane 1' is 3 minutes long with 6000000 streams

    >>> t1.listen()
    "Listening to 'TT' by TWICE"

    >>> t1.get_streams()
    6000001

    >>> p1 = Playlist('kpop', 'wtrang')
    >>> t1.add_to_playlist(p1)
    True

    >>> p1.get_title()
    'kpop'

    >>> p1.get_user()
    'wtrang'

    >>> p1.add_song(t1)
    False

    >>> p1.remove_song(t1)
    True

    >>> p1.add_song(t1)
    True

    >>> len(p1.get_songs())
    1

    >>> print(p1)
    Playlist 'kpop' by wtrang has 1 songs

    >>> [x.get_name() for x in p1.get_songs()]
    ['TT']

    >>> p1.get_total_streams()
    6000001

    >>> p1.get_total_length()
    3

    >>> p1.play()
    "Listening to 'TT' by TWICE"

    >>> p1.get_total_streams()
    6000002

    >>> p1.get_most_played_song()
    'TT'

    >>> t2 = Song('ASAP', 3.25, 'Staydom', 'STAYC', 1250000)
    >>> t2.listen()
    "Listening to 'ASAP' by STAYC"

    >>> p1.add_song(t2)
    True

    >>> p1.get_most_played_song()
    'TT'

    >>> [x.get_name() for x in p1.get_songs()]
    ['TT', 'ASAP']

    >>> p1.sort_songs('name')
    >>> [x.get_name() for x in p1.get_songs()]
    ['ASAP', 'TT']

    >>> print(p1.play())
    Listening to 'ASAP' by STAYC
    Listening to 'TT' by TWICE

    >>> p1.get_total_streams()
    7250005

    >>> p1.get_total_length()
    6.25

    >>> p1.remove_song(t2)
    True

    >>> p2 = Playlist('happy', 'zzhang')
    >>> p2.add_song(t1)
    True

    >>> p2.add_song(t2)
    True

    >>> p2.combine_playlists(p1)
    1

    >>> p2.remove_song(t1)
    True

    >>> p2.combine_playlists(p1)
    True

    >>> t1.add_to_playlist(p1)
    False

    >>> print(p2)
    Playlist 'happy' by zzhang has 2 songs

    >>> p2.remove_song(t1)
    True

    >>> t3 = Song('Panorama', 4, 'One-Reeler / Act IV', 'IZ*ONE', 10000000)
    >>> t3.listen()
    "Listening to 'Panorama' by IZ*ONE"

    >>> p3 = Playlist('banger', 'djun')
    >>> p3.add_song(41434)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> y = 14
    >>> p3.remove_song(y)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> x = 'traceer'
    >>> p3.combine_playlists(x)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> t3.add_to_playlist(x)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> t3.add_to_playlist(p3)
    True

    >>> p2.add_song(t1)
    True

    >>> p3.combine_playlists(p2)
    True

    >>> print(t2)
    'ASAP' by STAYC on 'Staydom' is 3.25 minutes long with 1250002 streams

    >>> print(t3)
    'Panorama' by IZ*ONE on 'One-Reeler / Act IV' is 4 minutes long with 10000001 streams

    >>> print(p3.play())
    Listening to 'Panorama' by IZ*ONE
    Listening to 'ASAP' by STAYC
    Listening to 'TT' by TWICE

    >>> p3.get_most_played_song()
    'Panorama'

    >>> p3.sort_songs('artist')
    >>> [s.get_artist() for s in p3.get_songs()]
    ['IZ*ONE', 'STAYC', 'TWICE']

    >>> p3.sort_songs(x)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> print(p3)
    Playlist 'banger' by djun has 3 songs

    >>> p3.get_total_length()
    10.25

    >>> p3.get_total_streams()
    17250009

    >>> p3.remove_song(t3)
    True

    >>> p3.get_most_played_song()
    'TT'
    """
    return


class Song:
    """
    Implementation of a song
    """
    platform = 'Spotify'

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song

        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        self.name = name
        self.length = length
        self.album = album
        self.artist = artist
        self.streams = streams


    def get_name(self):
        """ Getter for name attribute """
        return self.name


    def get_length(self):
        """ Getter for length attribute """
        return self.length


    def get_album(self):
        """ Getter for album attribute """
        return self.album


    def get_artist(self):
        """ Getter for artist attribute """
        return self.artist


    def get_streams(self):
        """ Getter for streams attribute """
        return self.streams


    def __str__(self):
        """
        String representation of Song
        """
        return '\'' + str(self.get_name()) + '\' by ' + \
            str(self.get_artist()) + ' on \'' + \
            self.get_album() + '\' is ' + str(self.get_length()) + \
                ' minutes long with ' + str(self.get_streams()) + ' streams'



    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        self.streams += 1
        return 'Listening to \'' + \
            self.get_name() + '\' by ' + self.get_artist()


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(playlist, Playlist)

        if self not in playlist.get_songs():
            playlist.add_song(self)
            return True
        return False


class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist

        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist

        Attributes:
        songs (list): list used to store songs in playlist
        """
        self.title = title
        self.user = user
        self.songs = []


    def get_title(self):
        """ Getter for title attribute """
        return self.title


    def get_user(self):
        """ Getter for user attribute """
        return self.user


    def get_songs(self):
        """ Getter for songs attribute """
        return self.songs


    def __str__(self):
        """
        String representation of Playlist
        """
        return 'Playlist \'' + self.get_title() + '\' by ' + \
            self.get_user() + ' has ' + \
                str(len(self.songs)) + ' songs'


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(song, Song)

        if song not in self.get_songs():
            self.songs.append(song)
            return True
        return False


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        assert isinstance(song, Song)

        if song in self.songs:
            self.songs.remove(song)
            return True
        return False


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        assert isinstance(sort_by, str)
        assert sort_by in ['name', 'length', 'album', 'artist', 'streams']

        self.songs.sort(key=lambda x: getattr(x, sort_by))


    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        return sum([song.get_streams() for song in self.get_songs()])


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        return sum([song.get_length() for song in self.get_songs()])


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that contains information on all the songs played.
        Format is specified in the writeup
        If the playlist is empty, return "Empty"
        """
        play_songs = ''
        if len(self.songs) == 0:
            return 'Empty'
        for song in self.get_songs():
            play_songs += song.listen() + '\n'
        return play_songs.strip()


    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True.
        If not, return the number of songs that weren't added.
        """
        assert isinstance(other_playlist, Playlist)

        init_songs = len(self.get_songs())

        [self.add_song(song) for song in other_playlist.get_songs()]

        if init_songs + \
            len(other_playlist.get_songs()) == len(self.get_songs()):
            return True
        return len(other_playlist.get_songs()) + \
            init_songs - len(self.get_songs())


    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        maximum = 0
        name = ''
        for song in self.get_songs():
            if song.get_streams() > maximum:
                maximum = song.get_streams()
                name = song.get_name()
        return name


################ RECURSION PART ##################

# Question 2.5

def type_with_number(message):
    """
    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'

    # Add your doctests below here #
    >>> type_with_number('aaaaaaaaAAAAaaaaa')
    '22222222222222222'

    >>> type_with_number('The quick brown fox jumps over the lazy dog.')
    '84307842502769603690586770683708430529903641'

    >>> type_with_number('wtrang')
    '987264'
    """
    num_dict = {
        ',': 1,
        '.': 1,
        '?': 1,
        '!': 1,
        'a': 2,
        'b': 2,
        'c': 2,
        'd': 3,
        'e': 3,
        'f': 3,
        'g': 4,
        'h': 4,
        'i': 4,
        'j': 5,
        'k': 5,
        'l': 5,
        'm': 6,
        'n': 6,
        'o': 6,
        'p': 7,
        'q': 7,
        'r': 7,
        's': 7,
        't': 8,
        'u': 8,
        'v': 8,
        'w': 9,
        'x': 9,
        'y': 9,
        'z': 9,
        ' ': 0
    }
    if len(message) == 1:
        return num_dict[message.lower()]
    return str(type_with_number(message[0])) + \
        str(type_with_number(message[1:]))


# Question 3.1

def create_palindrome_v1(start, end):
    """
    Creates a palindrome of integers starting from start, ending at end
    (in the middle) All inputs are positive integers. No input validation
    required.
    Parameters: start, end (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v1(1, 1)
    '1'
    >>> create_palindrome_v1(3, 5)
    '34543'
    >>> create_palindrome_v1(5, 2)
    '5432345'

    # Add your doctests below here #
    >>> create_palindrome_v1(5,6)
    '565'

    >>> create_palindrome_v1(5,5)
    '5'

    >>> create_palindrome_v1(9,1)
    '98765432123456789'
    """
    if start == end:
        return str(end)

    if start < end:
        return str(start) + \
            str(create_palindrome_v1(start+1, end)) + str(start)
    return str(start) + str(create_palindrome_v1(start-1, end)) + str(start)


def create_palindrome_v2(start1, end1, start2, end2):
    """
    Creates a two level palindrome of integers. The first level (outer level)
    starts from start1 and ends at end1. The second level (inner level) starts
    from start2 and end2. No input validation is required.
    Parameters: start1, end1, start2, end2 (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v2(1, 1, 1, 1)
    '1_1_1'
    >>> create_palindrome_v2(2, 5, 5, 4)
    '2345_545_5432'
    >>> create_palindrome_v2(3, 1, 5, 9)
    '321_567898765_123'

    # Add your doctests below here #
    >>> create_palindrome_v2(1, 3, 1, 4)
    '123_1234321_321'

    >>> create_palindrome_v2(3, 1, 4, 1)
    '321_4321234_123'

    >>> create_palindrome_v2(2, 2, 2, 0)
    '2_21012_2'
    """

    if start1 == end1:
        return str(start1) + '_' + \
            create_palindrome_v1(start2, end2) + '_' + str(start1)
    if start1 < end1:
        return str(start1) + \
            create_palindrome_v2(start1 + 1, end1, start2, end2) + str(start1)
    return str(start1) + \
        create_palindrome_v2(start1 - 1, end1, start2, end2) + str(start1)

# Question 4

def lutee_reproduction(n):
    """
    # Add your function description #

    >>> lutee_reproduction(1)
    2
    >>> lutee_reproduction(2)
    2
    >>> lutee_reproduction(3)
    4
    >>> lutee_reproduction(4)
    6
    >>> lutee_reproduction(6)
    16

    # Add your doctests below here #
    """

    # your code is here
