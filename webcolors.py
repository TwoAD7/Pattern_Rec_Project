"""
Utility functions for working with the color names and color value
formats defined by the HTML and CSS specifications for use in
documents on the Web.

See documentation (in docs/ directory of source distribution) for
details of the supported formats, conventions and conversions.

"""

import re
import string
from typing import NamedTuple, Tuple, Union


__version__ = "1.11.1"


def _reversedict(d: dict) -> dict:
    """
    Internal helper for generating reverse mappings; given a
    dictionary, returns a new dictionary with keys and values swapped.

    """
    return {value: key for key, value in d.items()}


HEX_COLOR_RE = re.compile(r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$")

HTML4 = "html4"
CSS2 = "css2"
CSS21 = "css21"
CSS3 = 'css3'

SUPPORTED_SPECIFICATIONS = (HTML4, CSS2, CSS21, CSS3)

SPECIFICATION_ERROR_TEMPLATE = "{{spec}} is not a supported specification for color name lookups; \
supported specifications are: {supported}.".format(
    supported=",".join(SUPPORTED_SPECIFICATIONS)
)

IntegerRGB = NamedTuple("IntegerRGB", [("red", int), ("green", int), ("blue", int)])
PercentRGB = NamedTuple("PercentRGB", [("red", str), ("green", str), ("blue", str)])
HTML5SimpleColor = NamedTuple(
    "HTML5SimpleColor", [("red", int), ("green", int), ("blue", int)]
)

IntTuple = Union[IntegerRGB, HTML5SimpleColor, Tuple[int, int, int]]
PercentTuple = Union[PercentRGB, Tuple[str, str, str]]


# Mappings of color names to normalized hexadecimal color values.
#################################################################

# The HTML 4 named colors.
#
# The canonical source for these color definitions is the HTML 4
# specification:
#
# http://www.w3.org/TR/html401/types.html#h-6.5
#
# The file tests/definitions.py in the source distribution of this
# module downloads a copy of the HTML 4 standard and parses out the
# color names to ensure the values below are correct.
HTML4_NAMES_TO_HEX = {
    "aqua": "#00ffff",
    "black": "#000000",
    "blue": "#0000ff",
    "fuchsia": "#ff00ff",
    "green": "#008000",
    "gray": "#808080",
    "lime": "#00ff00",
    "maroon": "#800000",
    "navy": "#000080",
    "olive": "#808000",
    "purple": "#800080",
    "red": "#ff0000",
    "silver": "#c0c0c0",
    "teal": "#008080",
    "white": "#ffffff",
    "yellow": "#ffff00",
}

# CSS 2 used the same list as HTML 4.
CSS2_NAMES_TO_HEX = HTML4_NAMES_TO_HEX

# CSS 2.1 added orange.
CSS21_NAMES_TO_HEX = {"orange": "#ffa500", **HTML4_NAMES_TO_HEX}

# The CSS 3/SVG named colors.
#
# The canonical source for these color definitions is the SVG
# specification's color list (which was adopted as CSS 3's color
# definition):
#
# http://www.w3.org/TR/SVG11/types.html#ColorKeywords
#
# CSS 3 also provides definitions of these colors:
#
# http://www.w3.org/TR/css3-color/#svg-color
#
# SVG provides the definitions as RGB triplets. CSS 3 provides them
# both as RGB triplets and as hexadecimal. Since hex values are more
# common in real-world HTML and CSS, the mapping below is to hex
# values instead. The file tests/definitions.py in the source
# distribution of this module downloads a copy of the CSS 3 color
# module and parses out the color names to ensure the values below are
# correct.
#Additional colors were found in file:///C:/Users/Owner/Desktop/Folders/Pattern_Rec/big-table.html
CSS3_NAMES_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50",
    "cornflowerblue": "#6495ed",
    "cornsilk": "#fff8dc",
    "crimson": "#dc143c",
    "cyan": "#00ffff",
    "darkblue": "#00008b",
    "darkcyan": "#008b8b",
    "darkgoldenrod": "#b8860b",
    "darkgray": "#a9a9a9",
    "darkgrey": "#a9a9a9",
    "darkgreen": "#006400",
    "darkkhaki": "#bdb76b",
    "darkmagenta": "#8b008b",
    "darkolivegreen": "#556b2f",
    "darkorange": "#ff8c00",
    "darkorchid": "#9932cc",
    "darkred": "#8b0000",
    "darksalmon": "#e9967a",
    "darkseagreen": "#8fbc8f",
    "darkslateblue": "#483d8b",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "darkturquoise": "#00ced1",
    "darkviolet": "#9400d3",
    "deeppink": "#ff1493",
    "deepskyblue": "#00bfff",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1e90ff",
    "firebrick": "#b22222",
    "floralwhite": "#fffaf0",
    "forestgreen": "#228b22",
    "fuchsia": "#ff00ff",
    "gainsboro": "#dcdcdc",
    "ghostwhite": "#f8f8ff",
    "gold": "#ffd700",
    "goldenrod": "#daa520",
    "gray": "#808080",
    "grey": "#808080",
    "green": "#008000",
    "greenyellow": "#adff2f",
    "honeydew": "#f0fff0",
    "hotpink": "#ff69b4",
    "indianred": "#cd5c5c",
    "indigo": "#4b0082",
    "ivory": "#fffff0",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightblue": "#add8e6",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgray": "#d3d3d3",
    "lightgrey": "#d3d3d3",
    "lightgreen": "#90ee90",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightskyblue": "#87cefa",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#b0c4de",
    "lightyellow": "#ffffe0",
    "lime": "#00ff00",
    "limegreen": "#32cd32",
    "linen": "#faf0e6",
    "magenta": "#ff00ff",
    "maroon": "#800000",
    "mediumaquamarine": "#66cdaa",
    "mediumblue": "#0000cd",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumslateblue": "#7b68ee",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "midnightblue": "#191970",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "navajowhite": "#ffdead",
    "navy": "#000080",
    "oldlace": "#fdf5e6",
    "olive": "#808000",
    "olivedrab": "#6b8e23",
    "orange": "#ffa500",
    "orangered": "#ff4500",
    "orchid": "#da70d6",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "peru": "#cd853f",
    "pink": "#ffc0cb",
    "plum": "#dda0dd",
    "powderblue": "#b0e0e6",
    "purple": "#800080",
    "red": "#ff0000",
    "rosybrown": "#bc8f8f",
    "royalblue": "#4169e1",
    "saddlebrown": "#8b4513",
    "salmon": "#fa8072",
    "sandybrown": "#f4a460",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "sienna": "#a0522d",
    "silver": "#c0c0c0",
    "skyblue": "#87ceeb",
    "slateblue": "#6a5acd",
    "slategray": "#708090",
    "slategrey": "#708090",
    "snow": "#fffafa",
    "springgreen": "#00ff7f",
    "steelblue": "#4682b4",
    "tan": "#d2b48c",
    "teal": "#008080",
    "thistle": "#d8bfd8",
    "tomato": "#ff6347",
    "turquoise": "#40e0d0",
    "violet": "#ee82ee",
    "wheat": "#f5deb3",
    "white": "#ffffff",
    "whitesmoke": "#f5f5f5",
    "yellow": "#ffff00",
    "yellowgreen": "#9acd32", "AliceBlue" :"#f0f8ff",
        "AntiqueWhite" :"#faebd7",
        "AntiqueWhite1" :"#ffefdb",
        "AntiqueWhite2" :"#eedfcc",
        "AntiqueWhite3" :"#cdc0b0",
        "AntiqueWhite4" :"#8b8378",
          "aquamarine1" :"#7fffd4",
          "aquamarine2" :"#76eec6",
          "aquamarine4" :"#458b74",
     "azure1":"#f0ffff",
"azure2":"#e0eeee",
"azure3":"#c1cdcd",
"azure4":"#838b8b",
"beige":"#f5f5dc",
"bisque1":"#ffe4c4",
"bisque2":"#eed5b7",
"bisque3":"#cdb79e",
"bisque4":"#8b7d6b",
"black":"#000000",
"lanchedAlmond":"#ffebcd",
"blue1":"#0000ff",
"blue2":"#0000ee",
"blue4":"#00008b",
"BlueViolet":"#8a2be2",
"brown":"#a52a2a",
"brown1":"#ff4040",
"brown2":"#ee3b3b",
"brown3":"#cd3333",
"brown4":"#8b2323",
"burlywood":"#deb887",
"burlywood1":"#ffd39b",
"burlywood2":"#eec591",
"burlywood3":"#cdaa7d",
"burlywood4":"#8b7355",
"CadetBlue":"#5f9ea0",
"CadetBlue1":"#98f5ff",
"CadetBlue2":"#8ee5ee",
"CadetBlue3":"#7ac5cd",
"CadetBlue4":"#53868b",
"chartreuse1":"#7fff00",
"chartreuse2":"#76ee00",
"chartreuse3":"#66cd00",
"chartreuse4":"#458b00",
"chocolate":"#d2691e",
"chocolate1":"#ff7f24",
"chocolate2":"#ee7621",
"chocolate3":"#cd661d",
"coral":"#ff7f50",
"coral1":"#ff7256",
"coral2":"#ee6a50",
"coral3":"#cd5b45",
"coral4":"#8b3e2f",
"CornflowerBlue":"#6495ed",
"cornsilk1":"#fff8dc",
"cornsilk2":"#eee8cd",
"cornsilk3":"#cdc8b1",
"cornsilk4":"#8b8878",
"cyan1":"#00ffff",
"cyan2":"#00eeee",
"cyan3":"#00cdcd",
"cyan4":"#008b8b",
"DarkGoldenrod":"#b8860b",
"DarkGoldenrod1":"#ffb90f",
"DarkGoldenrod2":"#eead0e",
"DarkGoldenrod3":"#cd950c",
"DarkGoldenrod4":"#8b6508",
"DarkGreen":"#006400",
"DarkKhaki":"#bdb76b",
"DarkOliveGreen":"#556b2f",
"DarkOliveGreen1":"#caff70",
"DarkOliveGreen2":"#bcee68",
"DarkOliveGreen3":"#a2cd5a",
"DarkOliveGreen4":"#6e8b3d",
"DarkOrange":"#ff8c00",
"DarkOrange1":"#ff7f00",
"DarkOrange2":"#ee7600",
"DarkOrange3":"#cd6600",
"DarkOrange4":"#8b4500",
"DarkOrchid":"#9932cc",
"DarkOrchid1":"#bf3eff",
"DarkOrchid2":"#b23aee",
"DarkOrchid3":"#9a32cd",
"DarkOrchid4":"#68228b",
"DarkSalmon":"#e9967a",
"DarkSeaGreen":"#8fbc8f",
"DarkSeaGreen1":"#c1ffc1",
"DarkSeaGreen2":"#b4eeb4",
"DarkSeaGreen3":"#9bcd9b",
"DarkSeaGreen4":"#698b69",
"DarkSlateBlue":"#483d8b",
"DarkSlateGray":"#2f4f4f",
"DarkSlateGray1":"#97ffff",
"DarkSlateGray2":"#8deeee",
"DarkSlateGray3":"#79cdcd",
"DarkSlateGray4":"#528b8b",
"DarkTurquoise":"#00ced1",
"DarkViolet":"#9400d3",
"DeepPink1":"#ff1493",
"DeepPink2":"#ee1289",
"DeepPink3":"#cd1076",
"DeepPink4":"#8b0a50",
"DeepSkyBlue1":"#00bfff",
"DeepSkyBlue2":"#00b2ee",
"DeepSkyBlue3":"#009acd",
"DeepSkyBlue4":"#00688b",
"DimGray":"#696969",
"DodgerBlue1":"#1e90ff",
"DodgerBlue2":"#1c86ee",
"DodgerBlue3":"#1874cd",
"DodgerBlue4":"#104e8b",
"firebrick":"#b22222",
"firebrick1":"#ff3030",
"firebrick2":"#ee2c2c",
"firebrick3":"#cd2626",
"firebrick4":"#8b1a1a",
"FloralWhite":"#fffaf0",
"ForestGreen":"#228b22",
"gainsboro":"#dcdcdc",
"GhostWhite":"#f8f8ff",
"gold1":"#ffd700",
"gold2":"#eec900",
"gold3":"#cdad00",
"gold4":"#8b7500",
"goldenrod":"#daa520",
"goldenrod1":"#ffc125",
"goldenrod2":"#eeb422",
"goldenrod3":"#cd9b1d",
"goldenrod4":"#8b6914",
"gray":"#bebebe",
"gray1":"#030303",
"gray10":"#1a1a1a",
"gray11":"#1c1c1c",
"gray12":"#1f1f1f",
"gray13":"#212121",
"gray14":"#242424",
"gray15":"#262626",
"gray16":"#292929",
"gray17":"#2b2b2b",
"gray18":"#2e2e2e",
"gray19":"#303030",
"gray2":"#050505",
"gray20":"#333333",
"gray21":"#363636",
"gray22":"#383838",
"gray23":"#3b3b3b",
"gray24":"#3d3d3d",
"gray25":"#404040",
"gray26":"#424242",
"gray27":"#454545",
"gray28":"#474747",
"gray29":"#4a4a4a",
"gray3":"#080808",
"gray30":"#4d4d4d",
"gray31":"#4f4f4f",
"gray32":"#525252",
"gray33":"#545454",
"gray34":"#575757",
"gray35":"#595959",
"gray36":"#5c5c5c",
"gray37":"#5e5e5e",
"gray38":"#616161",
"gray39":"#636363",
"gray4":"#0a0a0a",
"gray40":"#666666",
"gray41":"#696969",
"gray42":"#6b6b6b",
"gray43":"#6e6e6e",
"gray44":"#707070",
"gray45":"#737373",
"gray46":"#757575",
"gray47":"#787878",
"gray48":"#7a7a7a",
"gray49":"#7d7d7d",
"gray5":"#0d0d0d",
"gray50":"#7f7f7f",
"gray51":"#828282",
"gray52":"#858585",
"gray53":"#878787",
"gray54":"#8a8a8a",
"gray55":"#8c8c8c",
"gray56":"#8f8f8f",
"gray57":"#919191",
"gray58":"#949494",
"gray59":"#969696",
"gray6":"#0f0f0f",
"gray60":"#999999",
"gray61":"#9c9c9c",
"gray62":"#9e9e9e",
"gray63":"#a1a1a1",
"gray64":"#a3a3a3",
"gray65":"#a6a6a6",
"gray66":"#a8a8a8",
"gray67":"#ababab",
"gray68":"#adadad",
"gray69":"#b0b0b0",
"gray7":"#121212",
"gray70":"#b3b3b3",
"gray71":"#b5b5b5",
"gray72":"#b8b8b8",
"gray73":"#bababa",
"gray74":"#bdbdbd",
"gray75":"#bfbfbf",
"gray76":"#c2c2c2",
"gray77":"#c4c4c4",
"gray78":"#c7c7c7",
"gray79":"#c9c9c9",
"gray8":"#141414",
"gray80":"#cccccc",
"gray81":"#cfcfcf",
"gray82":"#d1d1d1",
"gray83":"#d4d4d4",
"gray84":"#d6d6d6",
"gray85":"#d9d9d9",
"gray86":"#dbdbdb",
"gray87":"#dedede",
"gray88":"#e0e0e0",
"gray89":"#e3e3e3",
"gray9":"#171717",
"gray90":"#e5e5e5",
"gray91":"#e8e8e8",
"gray92":"#ebebeb",
"gray93":"#ededed",
"gray94":"#f0f0f0",
"gray95":"#f2f2f2",
"gray97":"#f7f7f7",
"gray98":"#fafafa",
"gray99":"#fcfcfc",
"green1":"#00ff00",
"green2":"#00ee00",
"green3":"#00cd00",
"green4":"#008b00",
"GreenYellow":"#adff2f",
"honeydew1":"#f0fff0",
"honeydew2":"#e0eee0",
"honeydew3":"#c1cdc1",
"honeydew4":"#838b83",
"HotPink":"#ff69b4",
"HotPink1":"#ff6eb4",
"HotPink2":"#ee6aa7",
"HotPink3":"#cd6090",
"HotPink4":"#8b3a62",
"IndianRed":"#cd5c5c",
"IndianRed1":"#ff6a6a",
"IndianRed2":"#ee6363",
"IndianRed3":"#cd5555",
"IndianRed4":"#8b3a3a",
"ivory1":"#fffff0",
"ivory2":"#eeeee0",
"ivory3":"#cdcdc1",
"ivory4":"#8b8b83",
"khaki":"#f0e68c",
"khaki1":"#fff68f",
"khaki2":"#eee685",
"khaki3":"#cdc673",
"khaki4":"#8b864e",
"lavender":"#e6e6fa",
"LavenderBlush1":"#fff0f5",
"LavenderBlush2":"#eee0e5",
"LavenderBlush3":"#cdc1c5",
"LavenderBlush4":"#8b8386",
"LawnGreen":"#7cfc00",
"LemonChiffon1":"#fffacd",
"LemonChiffon2":"#eee9bf",
"LemonChiffon3":"#cdc9a5",
"LemonChiffon4":"#8b8970",
"light":"#eedd82",
"LightBlue":"#add8e6",
"LightBlue1":"#bfefff",
"LightBlue2":"#b2dfee",
"LightBlue3":"#9ac0cd",
"LightBlue4":"#68838b",
"LightCoral":"#f08080",
"LightCyan1":"#e0ffff",
"LightCyan2":"#d1eeee",
"LightCyan3":"#b4cdcd",
"LightCyan4":"#7a8b8b",
"LightGoldenrod1":"#ffec8b",
"LightGoldenrod2":"#eedc82",
"LightGoldenrod3":"#cdbe70",
"LightGoldenrod4":"#8b814c",
"LightGoldenrodYellow":"#fafad2",
"LightGray":"#d3d3d3",
"LightPink":"#ffb6c1",
"LightPink1":"#ffaeb9",
"LightPink2":"#eea2ad",
"LightPink3":"#cd8c95",
"LightPink4":"#8b5f65",
"LightSalmon1":"#ffa07a",
"LightSalmon2":"#ee9572",
"LightSalmon3":"#cd8162",
"LightSalmon4":"#8b5742",
"LightSeaGreen":"#20b2aa",
"LightSkyBlue":"#87cefa",
"LightSkyBlue1":"#b0e2ff",
"LightSkyBlue2":"#a4d3ee",
"LightSkyBlue3":"#8db6cd",
"LightSkyBlue4":"#607b8b",
"LightSlateBlue":"#8470ff",
"LightSlateGray":"#778899",
"LightSteelBlue":"#b0c4de",
"LightSteelBlue1":"#cae1ff",
"LightSteelBlue2":"#bcd2ee",
"LightSteelBlue3":"#a2b5cd",
"LightSteelBlue4":"#6e7b8b",
"LightYellow1":"#ffffe0",
"LightYellow2":"#eeeed1",
"LightYellow3":"#cdcdb4",
"LightYellow4":"#8b8b7a",
"LimeGreen":"#32cd32",
"linen":"#faf0e6",
"magenta":"#ff00ff",
"magenta2":"#ee00ee",
"magenta3":"#cd00cd",
"magenta4":"#8b008b",
"maroon":"#b03060",
"maroon1":"#ff34b3",
"maroon2":"#ee30a7",
"maroon3":"#cd2990",
"maroon4":"#8b1c62",
"medium":"#66cdaa",
"MediumAquamarine":"#66cdaa",
"MediumBlue":"#0000cd",
"MediumOrchid":"#ba55d3",
"MediumOrchid1":"#e066ff",
"MediumOrchid2":"#d15fee",
"MediumOrchid3":"#b452cd",
"MediumOrchid4":"#7a378b",
"MediumPurple":"#9370db",
"MediumPurple1":"#ab82ff",
"MediumPurple2":"#9f79ee",
"MediumPurple3":"#8968cd",
"MediumPurple4":"#5d478b",
"MediumSeaGreen":"#3cb371",
"MediumSlateBlue":"#7b68ee",
"MediumSpringGreen":"#00fa9a",
"MediumTurquoise":"#48d1cc",
"MediumVioletRed":"#c71585",
"MidnightBlue":"#191970",
"MintCream":"#f5fffa",
"MistyRose1":"#ffe4e1",
"MistyRose2":"#eed5d2",
"MistyRose3":"#cdb7b5",
"MistyRose4":"#8b7d7b",
"moccasin":"#ffe4b5",
"NavajoWhite1":"#ffdead",
"NavajoWhite2":"#eecfa1",
"NavajoWhite3":"#cdb38b",
"NavajoWhite4":"#8b795e",
"NavyBlue":"#000080",
"OldLace":"#fdf5e6",
"OliveDrab":"#6b8e23",
"OliveDrab1":"#c0ff3e",
"OliveDrab2":"#b3ee3a",
"OliveDrab4":"#698b22",
"orange1":"#ffa500",
"orange2":"#ee9a00",
"orange3":"#cd8500",
"orange4":"#8b5a00",
"OrangeRed1":"#ff4500",
"OrangeRed2":"#ee4000",
"OrangeRed3":"#cd3700",
"OrangeRed4":"#8b2500",
"orchid":"#da70d6",
"orchid1":"#ff83fa",
"orchid2":"#ee7ae9",
"orchid3":"#cd69c9",
"orchid4":"#8b4789",
"pale":"#db7093",
"PaleGoldenrod":"#eee8aa",
"PaleGreen":"#98fb98",
"PaleGreen1":"#9aff9a",
"PaleGreen2":"#90ee90",
"PaleGreen3":"#7ccd7c",
"PaleGreen4":"#548b54",
"PaleTurquoise":"#afeeee",
"PaleTurquoise1":"#bbffff",
"PaleTurquoise2":"#aeeeee",
"PaleTurquoise3":"#96cdcd",
"PaleTurquoise4":"#668b8b",
"PaleVioletRed":"#db7093",
"PaleVioletRed1":"#ff82ab",
"PaleVioletRed2":"#ee799f",
"PaleVioletRed3":"#cd6889",
"PaleVioletRed4":"#8b475d",
"PapayaWhip":"#ffefd5",
"PeachPuff1":"#ffdab9",
"PeachPuff2":"#eecbad",
"PeachPuff3":"#cdaf95",
"PeachPuff4":"#8b7765",
"pink":"#ffc0cb",
"pink1":"#ffb5c5",
"pink2":"#eea9b8",
"pink3":"#cd919e",
"pink4":"#8b636c",
"plum":"#dda0dd",
"plum1":"#ffbbff",
"plum2":"#eeaeee",
"plum3":"#cd96cd",
"plum4":"#8b668b",
"PowderBlue":"#b0e0e6",
"purple":"#a020f0",
"purple1":"#9b30ff",
"purple2":"#912cee",
"purple3":"#7d26cd",
"purple4":"#551a8b",
"red1":"#ff0000",
"red2":"#ee0000",
"red3":"#cd0000",
"red4":"#8b0000",
"RosyBrown":"#bc8f8f",
"RosyBrown1":"#ffc1c1",
"RosyBrown2":"#eeb4b4",
"RosyBrown3":"#cd9b9b",
"RosyBrown4":"#8b6969",
"RoyalBlue":"#4169e1",
"RoyalBlue1":"#4876ff",
"RoyalBlue2":"#436eee",
"RoyalBlue3":"#3a5fcd",
"RoyalBlue4":"#27408b",
"SaddleBrown":"#8b4513",
"salmon":"#fa8072",
"salmon1":"#ff8c69",
"salmon2":"#ee8262",
"salmon3":"#cd7054",
"salmon4":"#8b4c39",
"SandyBrown":"#f4a460",
"SeaGreen1":"#54ff9f",
"SeaGreen2":"#4eee94",
"SeaGreen3":"#43cd80",
"SeaGreen4":"#2e8b57",
"seashell1":"#fff5ee",
"seashell2":"#eee5de",
"seashell3":"#cdc5bf",
"seashell4":"#8b8682",
"sienna":"#a0522d",
"sienna1":"#ff8247",
"sienna2":"#ee7942",
"sienna3":"#cd6839",
"sienna4":"#8b4726",
"SkyBlue":"#87ceeb",
"SkyBlue1":"#87ceff",
"SkyBlue2":"#7ec0ee",
"SkyBlue3":"#6ca6cd",
"SkyBlue4":"#4a708b",
"SlateBlue":"#6a5acd",
"SlateBlue1":"#836fff",
"SlateBlue2":"#7a67ee",
"SlateBlue3":"#6959cd",
"SlateBlue4":"#473c8b",
"SlateGray":"#708090",
"SlateGray1":"#c6e2ff",
"SlateGray2":"#b9d3ee",
"SlateGray3":"#9fb6cd",
"SlateGray4":"#6c7b8b",
"snow1":"#fffafa",
"snow2":"#eee9e9",
"snow3":"#cdc9c9",
"snow4":"#8b8989",
"SpringGreen1":"#00ff7f",
"SpringGreen2":"#00ee76",
"SpringGreen3":"#00cd66",
"SpringGreen4":"#008b45",
"SteelBlue":"#4682b4",
"SteelBlue1":"#63b8ff",
"SteelBlue2":"#5cacee",
"SteelBlue3":"#4f94cd",
"SteelBlue4":"#36648b",
"tan":"#d2b48c",
"tan1":"#ffa54f",
"tan2":"#ee9a49",
"tan3":"#cd853f",
"tan4":"#8b5a2b",
"thistle":"#d8bfd8",
"thistle1":"#ffe1ff",
"thistle2":"#eed2ee",
"thistle3":"#cdb5cd",
"thistle4":"#8b7b8b",
"tomato1":"#ff6347",
"tomato2":"#ee5c42",
"tomato3":"#cd4f39",
"tomato4":"#8b3626",
"turquoise":"#40e0d0",
"turquoise1":"#00f5ff",
"turquoise2":"#00e5ee",
"turquoise3":"#00c5cd",
"turquoise4":"#00868b",
"violet":"#ee82ee",
"VioletRed":"#d02090",
"VioletRed1":"#ff3e96",
"VioletRed2":"#ee3a8c",
"VioletRed3":"#cd3278",
"VioletRed4":"#8b2252",
"wheat":"#f5deb3",
"wheat1":"#ffe7ba",
"wheat2":"#eed8ae",
"wheat3":"#cdba96",
"wheat4":"#8b7e66",
"white":"#ffffff",
"WhiteSmoke":"#f5f5f5",
"yellow1":"#ffff00",
"yellow2":"#eeee00",
"yellow3":"#cdcd00",
"yellow4":"#8b8b00",
"YellowGreen":"#9acd32",
}


# Mappings of normalized hexadecimal color values to color names.
#################################################################

HTML4_HEX_TO_NAMES = _reversedict(HTML4_NAMES_TO_HEX)

CSS2_HEX_TO_NAMES = HTML4_HEX_TO_NAMES

CSS21_HEX_TO_NAMES = _reversedict(CSS21_NAMES_TO_HEX)

CSS3_HEX_TO_NAMES = _reversedict(CSS3_NAMES_TO_HEX)

# CSS3 defines both 'gray' and 'grey', as well as defining either
# variant for other related colors like 'darkgray'/'darkgrey'. For a
# 'forward' lookup from name to hex, this is straightforward, but a
# 'reverse' lookup from hex to name requires picking one spelling.
#
# The way in which _reversedict() generates the reverse mappings will
# pick a spelling based on the ordering of dictionary keys, which
# varies according to the version and implementation of Python in use,
# and in some Python versions is explicitly not to be relied on for
# consistency. So here we manually pick a single spelling that will
# consistently be returned. Since 'gray' was the only spelling
# supported in HTML 4, CSS1, and CSS2, 'gray' and its varients are
# chosen.
CSS3_HEX_TO_NAMES["#a9a9a9"] = "darkgray"
CSS3_HEX_TO_NAMES["#2f4f4f"] = "darkslategray"
CSS3_HEX_TO_NAMES["#696969"] = "dimgray"
CSS3_HEX_TO_NAMES["#808080"] = "gray"
CSS3_HEX_TO_NAMES["#d3d3d3"] = "lightgray"
CSS3_HEX_TO_NAMES["#778899"] = "lightslategray"
CSS3_HEX_TO_NAMES["#708090"] = "slategray"


# Normalization functions.
#################################################################


def normalize_hex(hex_value: str) -> str:
    """
    Normalize a hexadecimal color value to 6 digits, lowercase.

    """
    match = HEX_COLOR_RE.match(hex_value)
    if match is None:
        raise ValueError(
            "'{}' is not a valid hexadecimal color value.".format(hex_value)
        )
    hex_digits = match.group(1)
    if len(hex_digits) == 3:
        hex_digits = "".join(2 * s for s in hex_digits)
    return "#{}".format(hex_digits.lower())


def _normalize_integer_rgb(value: int) -> int:
    """
    Internal normalization function for clipping integer values into
    the permitted range (0-255, inclusive).

    """
    return 0 if value < 0 else 255 if value > 255 else value


def normalize_integer_triplet(rgb_triplet: IntTuple) -> IntegerRGB:
    """
    Normalize an integer ``rgb()`` triplet so that all values are
    within the range 0-255 inclusive.

    """
    return IntegerRGB._make(_normalize_integer_rgb(value) for value in rgb_triplet)


def _normalize_percent_rgb(value: str) -> str:
    """
    Internal normalization function for clipping percent values into
    the permitted range (0%-100%, inclusive).

    """
    value = value.split("%")[0]
    percent = float(value) if "." in value else int(value)

    return "0%" if percent < 0 else "100%" if percent > 100 else "{}%".format(percent)


def normalize_percent_triplet(rgb_triplet: PercentTuple) -> PercentRGB:
    """
    Normalize a percentage ``rgb()`` triplet so that all values are
    within the range 0%-100% inclusive.

    """
    return PercentRGB._make(_normalize_percent_rgb(value) for value in rgb_triplet)


# Conversions from color names to various formats.
#################################################################


def name_to_hex(name: str, spec: str = CSS3) -> str:
    """
    Convert a color name to a normalized hexadecimal color value.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color of that name exists in the given specification,
    ``ValueError`` is raised.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise ValueError(SPECIFICATION_ERROR_TEMPLATE.format(spec=spec))
    normalized = name.lower()
    hex_value = {
        CSS2: CSS2_NAMES_TO_HEX,
        CSS21: CSS21_NAMES_TO_HEX,
        CSS3: CSS3_NAMES_TO_HEX,
        HTML4: HTML4_NAMES_TO_HEX,
    }[spec].get(normalized)
    if hex_value is None:
        raise ValueError(
            "'{name}' is not defined as a named color in {spec}".format(
                name=name, spec=spec
            )
        )
    return hex_value


def name_to_rgb(name: str, spec: str = CSS3) -> IntegerRGB:
    """
    Convert a color name to a 3-tuple of integers suitable for use in
    an ``rgb()`` triplet specifying that color.

    """
    return hex_to_rgb(name_to_hex(name, spec=spec))


def name_to_rgb_percent(name: str, spec: str = CSS3) -> PercentRGB:
    """
    Convert a color name to a 3-tuple of percentages suitable for use
    in an ``rgb()`` triplet specifying that color.

    """
    return rgb_to_rgb_percent(name_to_rgb(name, spec=spec))


# Conversions from hexadecimal color values to various formats.
#################################################################


def hex_to_name(hex_value: str, spec: str = CSS3) -> str:
    """
    Convert a hexadecimal color value to its corresponding normalized
    color name, if any such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color name for the value is found in the given
    specification, ``ValueError`` is raised.

    """
    if spec not in SUPPORTED_SPECIFICATIONS:
        raise ValueError(SPECIFICATION_ERROR_TEMPLATE.format(spec=spec))
    normalized = normalize_hex(hex_value)
    name = {
        CSS2: CSS2_HEX_TO_NAMES,
        CSS21: CSS21_HEX_TO_NAMES,
        CSS3: CSS3_HEX_TO_NAMES,
        HTML4: HTML4_HEX_TO_NAMES,
    }[spec].get(normalized)
    if name is None:
        raise ValueError("'{}' has no defined color name in {}".format(hex_value, spec))
    return name


def hex_to_rgb(hex_value: str) -> IntegerRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of integers
    suitable for use in an ``rgb()`` triplet specifying that color.

    """
    int_value = int(normalize_hex(hex_value)[1:], 16)
    return IntegerRGB(int_value >> 16, int_value >> 8 & 0xFF, int_value & 0xFF)


def hex_to_rgb_percent(hex_value: str) -> PercentRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of percentages
    suitable for use in an ``rgb()`` triplet representing that color.

    """
    return rgb_to_rgb_percent(hex_to_rgb(hex_value))


# Conversions from  integer rgb() triplets to various formats.
#################################################################


def rgb_to_name(rgb_triplet: IntTuple, spec: str = CSS3) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    return hex_to_name(rgb_to_hex(normalize_integer_triplet(rgb_triplet)), spec=spec)


def rgb_to_hex(rgb_triplet: IntTuple) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal value for that color.

    """
    return "#{:02x}{:02x}{:02x}".format(*normalize_integer_triplet(rgb_triplet))


def rgb_to_rgb_percent(rgb_triplet: IntTuple) -> PercentRGB:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of percentages suitable for use in
    representing that color.

    This function makes some trade-offs in terms of the accuracy of
    the final representation; for some common integer values,
    special-case logic is used to ensure a precise result (e.g.,
    integer 128 will always convert to '50%', integer 32 will always
    convert to '12.5%'), but for all other values a standard Python
    ``float`` is used and rounded to two decimal places, which may
    result in a loss of precision for some values.

    """
    # In order to maintain precision for common values,
    # special-case them.
    specials = {
        255: "100%",
        128: "50%",
        64: "25%",
        32: "12.5%",
        16: "6.25%",
        0: "0%",
    }
    return PercentRGB._make(
        specials.get(d, "{:.02f}%".format(d / 255.0 * 100))
        for d in normalize_integer_triplet(rgb_triplet)
    )


# Conversions from percentage rgb() triplets to various formats.
#################################################################


def rgb_percent_to_name(rgb_percent_triplet: PercentTuple, spec: str = CSS3) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    return rgb_to_name(
        rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet)), spec=spec
    )


def rgb_percent_to_hex(rgb_percent_triplet: PercentTuple) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal color value for that
    color.

    """
    return rgb_to_hex(
        rgb_percent_to_rgb(normalize_percent_triplet(rgb_percent_triplet))
    )


def _percent_to_integer(percent: str) -> int:
    """
    Internal helper for converting a percentage value to an integer
    between 0 and 255 inclusive.

    """
    return int(round(float(percent.split("%")[0]) / 100 * 255))


def rgb_percent_to_rgb(rgb_percent_triplet: PercentTuple) -> IntegerRGB:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of integers suitable for use in
    representing that color.

    Some precision may be lost in this conversion. See the note
    regarding precision for ``rgb_to_rgb_percent()`` for details.

    """
    return IntegerRGB._make(
        map(_percent_to_integer, normalize_percent_triplet(rgb_percent_triplet))
    )


# HTML5 color algorithms.
#################################################################

# These functions are written in a way that may seem strange to
# developers familiar with Python, because they do not use the most
# efficient or idiomatic way of accomplishing their tasks. This is
# because, for compliance, these functions are written as literal
# translations into Python of the algorithms in HTML5.
#
# For ease of understanding, the relevant steps of the algorithm from
# the standard are included as comments interspersed in the
# implementation.


def html5_parse_simple_color(input: str) -> HTML5SimpleColor:
    """
    Apply the simple color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    # 1. Let input be the string being parsed.
    #
    # 2. If input is not exactly seven characters long, then return an
    #    error.
    if not isinstance(input, str) or len(input) != 7:
        raise ValueError(
            "An HTML5 simple color must be a Unicode string "
            "exactly seven characters long."
        )

    # 3. If the first character in input is not a U+0023 NUMBER SIGN
    #    character (#), then return an error.
    if not input.startswith("#"):
        raise ValueError(
            "An HTML5 simple color must begin with the " "character '#' (U+0023)."
        )

    # 4. If the last six characters of input are not all ASCII hex
    #    digits, then return an error.
    if not all(c in string.hexdigits for c in input[1:]):
        raise ValueError(
            "An HTML5 simple color must contain exactly six ASCII hex digits."
        )

    # 5. Let result be a simple color.
    #
    # 6. Interpret the second and third characters as a hexadecimal
    #    number and let the result be the red component of result.
    #
    # 7. Interpret the fourth and fifth characters as a hexadecimal
    #    number and let the result be the green component of result.
    #
    # 8. Interpret the sixth and seventh characters as a hexadecimal
    #    number and let the result be the blue component of result.
    #
    # 9. Return result.
    return HTML5SimpleColor(
        int(input[1:3], 16), int(input[3:5], 16), int(input[5:7], 16)
    )


def html5_serialize_simple_color(simple_color: IntTuple) -> str:
    """
    Apply the serialization algorithm for a simple color from section
    2.4.6 of HTML5.

    """
    red, green, blue = simple_color

    # 1. Let result be a string consisting of a single "#" (U+0023)
    #    character.
    result = "#"

    # 2. Convert the red, green, and blue components in turn to
    #    two-digit hexadecimal numbers using lowercase ASCII hex
    #    digits, zero-padding if necessary, and append these numbers
    #    to result, in the order red, green, blue.
    format_string = "{:02x}"
    result += format_string.format(red)
    result += format_string.format(green)
    result += format_string.format(blue)

    # 3. Return result, which will be a valid lowercase simple color.
    return result


def html5_parse_legacy_color(input: str) -> HTML5SimpleColor:
    """
    Apply the legacy color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    # 1. Let input be the string being parsed.
    if not isinstance(input, str):
        raise ValueError(
            "HTML5 legacy color parsing requires a Unicode string as input."
        )

    # 2. If input is the empty string, then return an error.
    if input == "":
        raise ValueError("HTML5 legacy color parsing forbids empty string as a value.")

    # 3. Strip leading and trailing whitespace from input.
    input = input.strip()

    # 4. If input is an ASCII case-insensitive match for the string
    #    "transparent", then return an error.
    if input.lower() == "transparent":
        raise ValueError(
            u'HTML5 legacy color parsing forbids "transparent" as a value.'
        )

    # 5. If input is an ASCII case-insensitive match for one of the
    #    keywords listed in the SVG color keywords section of the CSS3
    #    Color specification, then return the simple color
    #    corresponding to that keyword.
    keyword_hex = CSS3_NAMES_TO_HEX.get(input.lower())
    if keyword_hex is not None:
        return html5_parse_simple_color(keyword_hex)

    # 6. If input is four characters long, and the first character in
    #    input is a "#" (U+0023) character, and the last three
    #    characters of input are all ASCII hex digits, then run these
    #    substeps:
    if (
        len(input) == 4
        and input.startswith("#")
        and all(c in string.hexdigits for c in input[1:])
    ):
        # 1. Let result be a simple color.
        #
        # 2. Interpret the second character of input as a hexadecimal
        #    digit; let the red component of result be the resulting
        #    number multiplied by 17.
        #
        # 3. Interpret the third character of input as a hexadecimal
        #    digit; let the green component of result be the resulting
        #    number multiplied by 17.
        #
        # 4. Interpret the fourth character of input as a hexadecimal
        #    digit; let the blue component of result be the resulting
        #    number multiplied by 17.
        result = HTML5SimpleColor(
            int(input[1], 16) * 17, int(input[2], 16) * 17, int(input[3], 16) * 17
        )

        # 5. Return result.
        return result

    # 7. Replace any characters in input that have a Unicode code
    #    point greater than U+FFFF (i.e. any characters that are not
    #    in the basic multilingual plane) with the two-character
    #    string "00".
    input = "".join("00" if ord(c) > 0xFFFF else c for c in input)

    # 8. If input is longer than 128 characters, truncate input,
    #    leaving only the first 128 characters.
    if len(input) > 128:
        input = input[:128]

    # 9. If the first character in input is a "#" (U+0023) character,
    #    remove it.
    if input.startswith("#"):
        input = input[1:]

    # 10. Replace any character in input that is not an ASCII hex
    #     digit with the character "0" (U+0030).
    input = "".join(c if c in string.hexdigits else "0" for c in input)

    # 11. While input's length is zero or not a multiple of three,
    #     append a "0" (U+0030) character to input.
    while (len(input) == 0) or (len(input) % 3 != 0):
        input += "0"

    # 12. Split input into three strings of equal length, to obtain
    #     three components. Let length be the length of those
    #     components (one third the length of input).
    length = int(len(input) / 3)
    red = input[:length]
    green = input[length : length * 2]
    blue = input[length * 2 :]

    # 13. If length is greater than 8, then remove the leading
    #     length-8 characters in each component, and let length be 8.
    if length > 8:
        red, green, blue = (red[length - 8 :], green[length - 8 :], blue[length - 8 :])
        length = 8

    # 14. While length is greater than two and the first character in
    #     each component is a "0" (U+0030) character, remove that
    #     character and reduce length by one.
    while (length > 2) and (red[0] == "0" and green[0] == "0" and blue[0] == "0"):
        red, green, blue = (red[1:], green[1:], blue[1:])
        length -= 1

    # 15. If length is still greater than two, truncate each
    #     component, leaving only the first two characters in each.
    if length > 2:
        red, green, blue = (red[:2], green[:2], blue[:2])

    # 16. Let result be a simple color.
    #
    # 17. Interpret the first component as a hexadecimal number; let
    #     the red component of result be the resulting number.
    #
    # 18. Interpret the second component as a hexadecimal number; let
    #     the green component of result be the resulting number.
    #
    # 19. Interpret the third component as a hexadecimal number; let
    #     the blue component of result be the resulting number.
    #
    # 20. Return result.
    return HTML5SimpleColor(int(red, 16), int(green, 16), int(blue, 16))
