from Tiles.onlyColorChangePixels import onlyColorChangePixels

class difficultyPixels:
    def get_pixels_based_on_dif(self, dif):
        colorChangePixels = onlyColorChangePixels()  
        if dif == 1:
            return colorChangePixels.cr1
        elif dif == 2:
            return colorChangePixels.cr2
        elif dif == 3:
            return colorChangePixels.cr3
        elif dif == 4:
            return colorChangePixels.cr4
        elif dif == 5:
            return colorChangePixels.cr5
        elif dif == 6:
            return colorChangePixels.cr6
        elif dif == 7:
            return colorChangePixels.cr7
        elif dif == 8:
            return colorChangePixels.cr8
        elif dif == 9:
            return colorChangePixels.cr9
        else:
            return colorChangePixels.cr1