class Codec:
    def __init__(self):
        # long : short
        self.encodeMap = {}
        # short : long
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            short = self.base + str(len(self.encodeMap) + 1)
            self.decodeMap[short] = longUrl
            self.encodeMap[longUrl] = short
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))