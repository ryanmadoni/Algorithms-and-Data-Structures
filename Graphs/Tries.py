from dataclasses import dataclass, field


@dataclass(slots=True)
class Trie(object):
    """
    A class to represent a Trie data structure.
    Intermediate nodes represent tokens and the end of full
    words have occurrence lists associated with them.
    """

    # Define data class properties.  Token is the token
    # associated with the Trie.  Occurrence list is a
    # list of documents that are relevent to token.
    # Children is the list of other Tries this Trie has.
    # Start a defualt nodes value to "$ROOT$" as a sentinel value.
    token: str = field(default_factory=lambda: "$ROOT$")
    occurrenceList: list[str] = field(default_factory=lambda: [])
    children: list["Trie"] = field(default_factory=lambda: [],
                                             init=False)
    

    def add(self, token: str, occurrenceList: list[str]) -> None:
        """
        A function to add a token to the current Trie.
        """

        # Check if the token is the empty string.
        if token == "":

            # Add the occurrence list since we
            # reached the end of a token and return.
            self.occurrenceList = occurrenceList
            return

        # Loop for all children of the current Trie.
        # If the loop completes then we must create
        # a new child, i.e., enter the else statement.
        for child in self.children:

            # Check if the current value is already a child
            # and if it is, then recurse down the tree and
            # break so we do not enter the else.
            if token[0] == child.token:
                child.add(token[1:], occurrenceList)
                break
        else:
            
            # Check if this will be the last Trie added and add
            # the occurrence list if it is.  Otherwise, add the
            # new Trie as a child and recurse down the Trie.
            if len(token) == 1:
                self.children.append(Trie(token[0], occurrenceList))
            else:
                self.children.append(Trie(token[0]))
                self.children[-1].add(token[1:], occurrenceList)


    def compress(self) -> "Trie":
        """
        Compresses a Trie so that it uses fewer nodes to function, by
        compressing single character nodes into multicharacter tokens.
        """

        # Base case for if there are no
        # children.  Return the current Trie.
        if self.children == []:
            return self
        
        # If there are more then one child
        # of this Trie, compress them all.
        if len(self.children) > 1:
            self.children = [child.compress()
                             for child in self.children]
            return self
        
        # If there is one child and this Trie is not
        # the end of a unique token, then we can compress.
        if len(self.children) == 1 and self.occurrenceList == []:

            # Compress tokens, propogate occurence
            # list and children, then compress again.
            self.token += self.children[0].token
            self.occurrenceList = self.children[0].occurrenceList
            self.children = self.children[0].children
            return self.compress()

        # This Trie is the end of a unique token and has
        # one child, so only compress its one children.
        self.children[0] = self.children[0].compress()
        return self


    def search(self, token: str) -> list[tuple[float, str]]:
        """
        A function to search the Trie and return the
        occurenceList associated with a given token.
        """

        # If the token is empty, return the occurrence
        # list associated with the current Trie.
        if token == "":
            return self.occurrenceList

        # Loop for all children of the current Trie.
        # If the loop completes then the token is not
        # in the Trie, i.e., enter the else statement.
        for child in self.children:

            # Check if the current value is already a child
            # and if it is, then recurse down the tree.
            if token.startswith(child.token):
                return child.search(token[len(child.token):])
        else:
            return []