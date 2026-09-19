import string
import random

letters = string.ascii_letters.lower()
numbers = string.digits
underscore = "_"

def gen(option, length=None):
    if option.lower() in ["four", "five"]:
        size = 4 if option.lower() == "four" else 5

        extra_pool = random.choice([numbers, underscore])
        pool = letters + extra_pool

        username = ''.join(random.choice(pool) for _ in range(size))

        if not all(c in letters for c in username):
            return username

    elif option.lower() == "words":
    	word_list = [
        	"angel", "baby", "pretty", "sweet", "dream", "love",
        	"lucky", "magic", "heaven", "cloud", "moon", "star",
        	"sun", "sky", "rain", "snow", "mist", "glow",
        	"light", "dark", "night", "dawn", "dusk", "sunset",
        	"sunrise", "midnight", "starlight", "moonlight",
        	"life", "time", "word", "world", "heart", "soul",
        	"mind", "hope", "wish", "memory", "future", "past",
        	"dream", "moment", "story", "secret", "forever",
        	"always", "never", "again", "alone", "together",
        	"pillow", "mirror", "phone", "camera", "letter",
        	"paper", "book", "rose", "flower", "ribbon", "silk",
        	"velvet", "candle", "coffee", "sugar", "honey",
        	"cherry", "peach", "berry", "vanilla", "crystal",
        	"silver", "gold", "diamond", "pearl",
        	"ocean", "river", "lake", "island", "garden", "forest",
        	"summer", "winter", "spring", "autumn", "desert",
        	"valley", "meadow", "garden", "paradise", "castle",
        	"city", "street", "home", "house",
        	"wild", "free", "lost", "young", "real", "true",
        	"soft", "calm", "quiet", "loud", "pretty", "lovely",
        	"golden", "blue", "pink", "red", "white", "black",
        	"purple", "silver", "classic", "rare", "special",
        	"little", "tiny", "big", "forever",
        	"dior", "prada", "chanel", "gucci", "vogue", "model",
        	"style", "fashion", "glam", "luxury", "icon",
        	"angelic",
        	"last", "first", "new", "old", "next", "lost",
        	"found", "real", "only", "just", "true", "your",
        	"my", "little", "big", "one", "two", "zero",
        	"hello", "goodbye", "sorry", "maybe", "never",
        	"always", "still", "back", "home", "away"
    	]

    	word1, word2 = random.sample(word_list, 2)
    	return word1 + word2

    elif option.lower() == "random":
        return ''.join(random.choice(letters) for _ in range(8))

    elif option.lower() == "numbers":
        return ''.join(random.choice(numbers) for _ in range(4))

    elif option.lower() == "lnb":
        if length is None or length < 2:
            raise ValueError("Length must be at least 2 for lnb")

        chars = [
            random.choice(letters),
            random.choice(numbers),
        ]

        pool = letters + numbers
        chars += [random.choice(pool) for _ in range(length - 2)]

        random.shuffle(chars)
        return ''.join(chars)
