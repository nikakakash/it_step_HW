

class Convertor:

    def convert(self,numbers):
        intList=[]
        roman_numeral = numbers
        separated_characters = list(roman_numeral)
        total=0
        prev_Val=0
        for character in separated_characters:
            character = character.replace('M',str(1000))
            character = character.replace('L',str(50))
            character = character.replace('D', str(500))
            character = character.replace('C', str(100))
            character = character.replace('X', str(10))
            character = character.replace('V', str(5))
            character = character.replace('I', str(1))
            intList.append(int(character))
        for nums in reversed(intList):
            if nums < prev_Val:
                total -= nums
            else:
                total += nums
            prev_Val = nums
        return total



converter = Convertor()
print(converter.convert('MMCML'))
