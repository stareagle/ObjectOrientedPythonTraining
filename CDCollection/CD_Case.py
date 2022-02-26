last_cd_id = 0


class CD:
    """
    Describes a physical CD
    """
    def __init__(self, title, pub_year, length):
        """
        Initialises a cd with basic information (title, pub_year, length) and sets the checked out flag to false and
        the borrower to blank string
        :param title: String
        :param pub_year: String
        :param length: Int
        """
        self.title = title
        self.pub_year = pub_year
        self.length_minutes = length
        self.checked_out = False
        self.borrower = ''
        global last_cd_id
        last_cd_id += 1
        self.cd_id = last_cd_id

    def match(self, search_field, filter):
        """
        Depending on the value of the search_field the appropriate attribute is searcged and matched to the filter
        parameter and if matches returns true.
        :param search_field: String
        :param filter: String
        :return:
        """
        if search_field == 'T':
            return filter in self.title
        elif search_field == 'P':
            return str(filter) in self.pub_year
        elif search_field == 'L':
            return str(filter) in str(self.length_minutes)
        elif search_field == 'C':
            return filter in self.checked_out
        elif search_field == 'B':
            return filter in self.borrower


class CDCase:
    """
    Describes the wooden case holding multiple CDs
    """
    def __init__(self):
        """
        Creates an empty list of cds
        """
        self.cds = []

    def new_cd(self, title, pub_year, length):
        """
        Creates a new entry into the list of CDs
        :param title: String
        :param pub_year: String
        :param length: String
        :return:
        """
        self.cds.append(CD(title, pub_year, length))

    def print_cds(self):
        for cd in self.cds:
            print("{}: {}".format(cd.cd_id, cd.title))

    def delete_cd(self, cd_id):
        pass

    def check_out_cd(self, cd_id):
        pass

    def _find_cd(self, cd_id):
        for cd in self.cds:
            if cd.cd_id == cd_id:
                return cd



