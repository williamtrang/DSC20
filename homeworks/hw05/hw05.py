"""
DSC20 WI22 HW05
Name: William Trang
PID: A16679845
"""

# begin helper methods
def ceil(x):
    """
    Simulation to math.ceil
    No doctest needed
    """
    if int(x) != x:
        return int(x) + 1
    return int(x)

def log(x):
    """
    Simulation to math.log with base e
    No doctests needed
    """
    n = 1e10
    return n * ((x ** (1/n)) - 1)
# end helper methods

# Question1
def db_calc(dynamic, inst_mult):
    """
    Given a musical dynamic abbreviation as a string and a 
    multiplier inst_mult for louder and softer instruments 
    as a float, compute the intial decibel level based on
    distance from the instrument.

    Parameters:
        dynamic: Abbreviation of music dynamic.
        inst_mult: Multiplier for louder/softer instruments.
    Returns:
        Function that computes intial decibel level of
        instrument for a given distance.

    >>> snare_1 = db_calc('ff',  1.2)
    >>> snare_1(0)
    126
    >>> snare_1(10)
    80
    >>> snare_1(50)
    48
    >>> db_calc('loud', 1)(35)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> db_calc('pp', 1.200001)(50)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> snare_2 = db_calc('p', 1.3)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> snare_3 = db_calc('pp', 1)
    >>> snare_3(10)
    0
    >>> snare_4 = db_calc('pp', 'cha')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(dynamic, str)
    assert isinstance(inst_mult, float) or isinstance(inst_mult, int)
    assert (inst_mult >= .8) and (inst_mult <= 1.2)
    
    db = {'pp': 30,
          'p': 45, 
          'mp': 60,
          'mf': 75,
          'f': 90,
          'ff': 105}

    assert dynamic in db

    db_init = db[dynamic] * inst_mult

    def db_level(distance):
        """
        Computes the observed decibel level given
        a distance away from the instrument.

        Parameters:
            distance: Distance away from the instrument as an integer.
        Returns:
            Decibel level for given distance from instrument as an integer.
        """
        assert isinstance(distance, int)
        assert distance >= 0

        if distance == 0:
            return round(db_init)
        level = db_init - 20 * log(distance)
        if level < 0:
            return 0
        return round(level)

    return db_level


# Question2
def next_move(file_names, decision):
    """
    Takes in a filepath containing constestant names and decisions,
    and a final decision to make. Returns a message for the
    contestants whose decisions match the final decisions.

    Parameters:
        file_names: Path to file containing names and decisions.
        decision: Final decision that determines which contestants
        are sent messages.
    Returns:
        Function that creates message for contestants
        that match the final decision.

    >>> message_to_students = next_move("files/names.txt", "h")
    >>> mess = message_to_students("Never give up!")
    >>> print(mess)
    Dear I!
    Unfortunately, it is time to go home. Never give up!
    >>> message_to_students = next_move("files/names.txt", "s")
    >>> mess = message_to_students("San Diego, Earth.")
    >>> print(mess)
    Dear A, C, E, G, K!
    We are happy to announce that you can move to the next round.
    It will be held at San Diego, Earth.

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> message_2 = next_move('files/names2.txt', 'h')
    >>> mess2 = message_2('It is all good.')
    >>> print(mess2)
    Dear Will, M!
    Unfortunately, it is time to go home. It is all good.
    >>> message_2 = next_move('files/names2.txt', 's')
    >>> mess2 = message_2('Yay!')
    >>> print(mess2)
    Dear Zhi!
    We are happy to announce that you can move to the next round.
    It will be held at Yay!
    >>> mess2 = message_2('MOS114')
    >>> print(mess2)
    Dear Zhi!
    We are happy to announce that you can move to the next round.
    It will be held at MOS114
    """
    f_name = 0
    dec_index = 3
    name_list = []
    tmp = ''

    with open(file_names, 'r') as f:
        for line in f:
            tmp = line.split(',')
            if tmp[dec_index].strip().lower() == decision.lower():
                name_list.append(tmp[f_name])
    def final_message(message):
        """
        Creates and returns a string final_message based
        on an inputted message.

        Parameters:
            message: Custom message to send to participants
            matching the decision.
        Returns:
            A predetermined string message along with the custom
            message to send.
        """
        output_str = 'Dear ' + ', '.join(name_list) + '!\n'
        if decision == 's':
            output_str += 'We are happy to announce that you can \
move to the next round.\nIt will be held at \
' + message
        else:
            output_str += 'Unfortunately, it is time to go home. ' + message
        return output_str
    return final_message

# Question3
def forge(filepath):
    """
    Reads a given filepath containing names and votes
    with votes being 1 and 0, and changes people's votes
    in the file to make the majority vote what is desired.

    Parameters:
        filepath: Path to file containing names and votes.
    Returns:
        Function that forges votes in the file.

	>>> forge('files/vote1.txt')(0)
    >>> with open('files/vote1.txt', 'r') as outfile1:
    ...     print(outfile1.read().strip())
    Jerry,0
    Larry,0
    Colin,0
    Scott,0
    Jianming,0
    Huaning,1
    Amy,1
    Elvy,1
    >>> forge('files/vote2.txt')(0)
    >>> with open('files/vote2.txt', 'r') as outfile2:
    ...     print(outfile2.read().strip())
    Jerry,0
    Larry,0
    Colin,0
    Scott,1
    Jianming,0
    Huaning,1
    Amy,1
    Elvy,0
    >>> forge('files/vote3.txt')(1)
    >>> with open('files/vote3.txt', 'r') as outfile3:
    ...     print(outfile3.read().strip())
    Jerry,1
    Larry,1
    Colin,1
    Scott,0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> forge('files/vote4.txt')(1)
    >>> with open('files/vote4.txt', 'r') as outfile4:
    ...     print(outfile4.read().strip())
    Will,1
    Zhi,1
    TL,1
    DJ,0
    Rj,0
    RD,1
    >>> forge('files/vote5.txt')(0)
    >>> with open('files/vote5.txt', 'r') as outfile5:
    ...     print(outfile5.read().strip())
    Will,0
    Zhi,0
    TL,1
    DJ,0
    Rj,0
    RD,1
    >>> forge('files/vote6.txt')(1)
    >>> with open('files/vote6.txt', 'r') as outfile6:
    ...     print(outfile6.read().strip())
    Will,1
    """
    votes = {0: 0,
             1: 0}
    vote_index = 1
    name_index = 0

    with open(filepath, 'r') as f:
        for line in f:
            votes[int(line.split(',')[vote_index])] += 1
       
    majority = int((votes[0] + votes[1]) / 2) + 1
    def change_votes(wanted):
        """
        Takes in a vote that is the desired result of the
        voting process. Write to the file to make the wanted
        vote the majority vote.

        Parameters:
            wanted: The desired majority in the voting process.
        """
        votes_to_change = majority - votes[wanted]
        new_votes = ''
        with open(filepath, 'r') as f:
            for line in f:
                if votes_to_change > 0:
                    if int(line.split(',')[vote_index]) != int(wanted):
                        new_votes += line.split(',')[name_index] + ',' + str(wanted) + '\n'
                        votes_to_change -= 1
                    else:
                        new_votes += line
                else:
                    new_votes += line
        with open(filepath, 'w') as f:
            f.write(new_votes)

    return change_votes

# Question4.1
def number_of_adults_1(lst, age = 18):
    """
    Takes in a list of integers containing ages
    and an age threshold, and returns the number of
    adults needed to supervise people below the
    age threshold. Each adult can supervise three people.

    Parameters:
        lst: List containing ages of people as integers.
        age: Age threshold where people no longer need
        supervision. Default value is 18.
    Returns:
        Number of adults needed to supervise people under
        the age threshold.

    >>> number_of_adults_1([1,2,3,4,5,6,7])
    3
    >>> number_of_adults_1([1,2,3,4,5,6,7], 5)
    2
    >>> number_of_adults_1([1,2,3,4,5,6,7], age = 2)
    1
    
    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    adults_per_kid = 3
    return ceil(len([ages for ages in lst if ages < age]) / adults_per_kid)

# Question4.2
def number_of_adults_2(*args):
    """
    Takes in positional arguments of integer ages,
    and returns the number of adults needed to supervise
    people below the age threshold which is 18. One adult
    can supervise three people.

    Parameters:
        *args: Positional arguments that designate age.
    Returns:
        Number of adults needed to supervise people below
        eighteen years old.

    >>> number_of_adults_2(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_2(10,20,13,4)
    1
    >>> number_of_adults_2(19, 20)
    0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    adults_per_kid = 3
    age_threshold = 18
    return ceil(len([ages for ages in args if ages < age_threshold]) / adults_per_kid)

# Question4.3
def number_of_adults_3(*args, age = 18):
    """
    Takes in positional arguments of integer ages,
    and returns the number of adults needed to supervise
    people below the given age threshold. One adult
    can supervise three people.

    Parameters:
        *args: Positional arguments that designate age.
        age: Age threshold where people no longer need
        supervision. Default value is 18.
    Returns:
        Number of adults needed to supervise people below
        age threshold.

    >>> number_of_adults_3(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 5)
    2
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 2)
    1

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    adults_per_kid = 3
    return ceil(len([ages for ages in args if ages < age]) / adults_per_kid)

# Question5
def school_trip(age_limit, **kwargs):
    """
    Given a set of keyword arguments with key being each class and
    the values being ages in the class, return a dictionary where
    keys are classes and values are the number of adults needed to
    supervise the people in the class. Kids below the age limit need
    supervision and adults can supervise up to 3 kids.

    Parameters:
        age_limit: Age threshold where people no longer need supervision.
        **kwargs: Keyword arguments where key is class and values
        are a list of ages in the class.
    Returns:
        Dictionary where keys are classes and values are number of adults
        needed to supervise the class.

    >>> school_trip(14, class1=[1,2,3], class2 =[4,5,6,7], class3=[15,16])
    {'class1': 1, 'class2': 2, 'class3': 0}
    >>> school_trip(14, class1=[21,3], class2 =[41,1,2,24,6], class3=[30,3,1,7,88])
    {'class1': 1, 'class2': 1, 'class3': 1}
    >>> school_trip(100, class1=[21,3], class2 =[41,1000,2,24,6], class3=[3,1,7,88])
    {'class1': 1, 'class2': 2, 'class3': 2}

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    trip = []
    for keys, values in kwargs.items():
        trip.append((keys, number_of_adults_3(*values, age = age_limit)))
    return dict(trip)

# Question6
def rearrange_args(*args, **kwargs):
    """
    Given positional arguments and keyword arguments, return a list
    of tuples containing the type of argument and number of the
    argument as well as its value.

    Parameters:
        *args: Random positional arguments.
        **kwargs: Random keyword arguments.
    Returns:
        List of tuples where the first value of the tuple is the
        type of argument with its number and the second value is
        the value of the argument. Keyword arguments' first value
        also contains the key of the keyword argument.

    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    key_index = 0
    val_index = 1
    return [('positional_' + str(count), arg) for count, arg in list(enumerate(args))] \
        + [('keyword_' + str(num) + '_' + dic[key_index], dic[val_index]) \
            for num, dic in enumerate(kwargs.items())]
