"""
DSC 20 Homework 07
Name: TODO
PID:  TODO
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

    """
    return


class Song:
    """
    Implementation of a song
    """
    # TODO: Initialize class attribute
    platform = ...

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
        # YOUR CODE STARTS HERE #


    def get_name(self):
        """ Getter for name attribute """
        # YOUR CODE STARTS HERE #


    def get_length(self):
        """ Getter for length attribute """
        # YOUR CODE STARTS HERE #


    def get_album(self):
        """ Getter for album attribute """
        # YOUR CODE STARTS HERE #


    def get_artist(self):
        """ Getter for artist attribute """
        # YOUR CODE STARTS HERE #


    def get_streams(self):
        """ Getter for streams attribute """
        # YOUR CODE STARTS HERE #


    def __str__(self):
        """
        String representation of Song
        """
        # YOUR CODE STARTS HERE #


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        # YOUR CODE STARTS HERE #


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        # YOUR CODE STARTS HERE #


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
        # YOUR CODE STARTS HERE #


    def get_title(self):
        """ Getter for title attribute """
        # YOUR CODE STARTS HERE #


    def get_user(self):
        """ Getter for user attribute """
        # YOUR CODE STARTS HERE #


    def get_songs(self):
        """ Getter for songs attribute """
        # YOUR CODE STARTS HERE #


    def __str__(self):
        """
        String representation of Playlist
        """
        # YOUR CODE STARTS HERE #


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        # YOUR CODE STARTS HERE #


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        # YOUR CODE STARTS HERE #


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        # YOUR CODE STARTS HERE #


    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        # YOUR CODE STARTS HERE #


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        # YOUR CODE STARTS HERE #


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that contains information on all the songs played.
        Format is specified in the writeup
        If the playlist is empty, return "Empty"
        """
        # YOUR CODE STARTS HERE #


    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        # YOUR CODE STARTS HERE #
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        # YOUR CODE STARTS HERE #


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

    """
    # your code is here



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

    """
    # your code is here



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

    """
    # your code is here

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
