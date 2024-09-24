import random
import time
import sys
import os

import cmd_RobCo
import var_RobCo
import sys_RobCo
import termS_RobCo
import mainCode_RobCo


def t_inquire_code():
    cmd_RobCo.char("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL \nENTER PASSWORD NOW")
    with open('system/sevenletterwords.txt') as wordListFile:
        WORDS = wordListFile.readlines()
    for i in range(len(WORDS)):
        WORDS[i] = WORDS[i].strip().upper()

    def main():
        input('\nPress enter to begin protocol...')
        termS_RobCo.empty()

        gameWords = getWords()
        computerMemory = getComputerMemoryString(gameWords)
        secretPassword = random.choice(gameWords)

        cmd_RobCo.char(computerMemory)
        for triesRemaining in range(4, 0, -1):
            playerMove = askForPlayerGuess(gameWords, triesRemaining)
            if playerMove == secretPassword:
                cmd_RobCo.char("\nACCESS GRANTED")
                sys_RobCo.log(3, 102, '')

                mainCode_RobCo.main_code()
                return
            else:
                numMatches = numMatchingLetters(secretPassword, playerMove)
                cmd_RobCo.char('\nAccess Denied ({}/7 correct)'.format(numMatches))
        cmd_RobCo.char('Out of tries.')
        time.sleep(1)
        cmd_RobCo.clear()
        sys_RobCo.log(3, 83, '')

        print("\n" * 14)
        cmd_RobCo.char("TERMINAL LOCKED".center(var_RobCo.centre, " "))
        termS_RobCo.empty()

        cmd_RobCo.char("PLEASE CONTACT AN ADMINISTRATOR".center(var_RobCo.centre))
        termS_RobCo.empty()
        time.sleep(10)
        cmd_RobCo.char("RESTARTING OS_SYSTEM")
        sys_RobCo.log(3, 84, '')
        os.system("sudo shutdown -h now")

    def getWords():
        secretPassword = random.choice(WORDS)
        words = [secretPassword]

        while len(words) < 3:
            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 0:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 5:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 3:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 12:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) != 0:
                words.append(randomWord)

        while len(words) < 12:
            randomWord = getOneWordExcept(words)
            words.append(randomWord)

        assert len(words) == 12
        return words

    def getOneWordExcept(blocklist=None):
        if blocklist is None:
            blocklist = []

        while True:
            randomWord = random.choice(WORDS)
            if randomWord not in blocklist:
                return randomWord

    def numMatchingLetters(word1, word2):
        matches = 0
        for a in range(len(word1)):
            if word1[a] == word2[a]:
                matches += 1
            return matches

    def getComputerMemoryString(words):
        linesWithWords = random.sample(range(16 * 2), len(words))
        memoryAddress = 16 * random.randint(0, 4000)

        computerMemory = []
        nextWord = 0
        for lineNum in range(16):
            leftHalf = ''
            rightHalf = ''
            for j in range(16):
                leftHalf += random.choice(var_RobCo.GARBAGE_CHARS)
                rightHalf += random.choice(var_RobCo.GARBAGE_CHARS)

            if lineNum in linesWithWords:
                insertionIndex = random.randint(0, 9)
                leftHalf = (leftHalf[:insertionIndex] + words[nextWord] + leftHalf[insertionIndex + 7:])
                nextWord += 1

            if lineNum + 16 in linesWithWords:
                insertionIndex = random.randint(0, 9)
                rightHalf = (rightHalf[:insertionIndex] + words[nextWord] + rightHalf[insertionIndex + 7:])
                nextWord += 1

            computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                                  + '  ' + leftHalf + '    '
                                  + '0x' + hex(memoryAddress + (16 * 16))[2:].zfill(4)
                                  + '  ' + rightHalf)

            memoryAddress += 16

        return '\n'.join(computerMemory)

    def askForPlayerGuess(words, tries):
        while True:
            cmd_RobCo.char('\nEnter password: ({} tries remaining)'.format(tries))
            guess = input('> ').upper()
            if guess in words:
                return guess
            cmd_RobCo.char('That is not one of the possible passwords listed above')
            cmd_RobCo.char('Try entering "{}" or "{}".'.format(words[0], words[1]))

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()


def t_inquire_sim(simulationText):
    termS_RobCo.slide_up()

    cmd_RobCo.char("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL \nENTER PASSWORD NOW")
    with open(simulationText) as wordListFile:
        WORDS = wordListFile.readlines()
    for i in range(len(WORDS)):
        WORDS[i] = WORDS[i].strip().upper()

    def main():
        input('\nPress enter to begin protocol...')
        termS_RobCo.empty()

        gameWords = getWords()
        computerMemory = getComputerMemoryString(gameWords)
        secretPassword = random.choice(gameWords)

        cmd_RobCo.char(computerMemory)
        for triesRemaining in range(4, 0, -1):
            playerMove = askForPlayerGuess(gameWords, triesRemaining)
            if playerMove == secretPassword:
                cmd_RobCo.char("ACCESS GRANTED")
                termS_RobCo.slide_up()

                return
            else:
                numMatches = numMatchingLetters(secretPassword, playerMove)
                cmd_RobCo.char('Access Denied ({}/7 correct)'.format(numMatches))
        cmd_RobCo.char('Out of tries. Secret password was {}.'.format(secretPassword))
        time.sleep(1)

    def getWords():
        secretPassword = random.choice(WORDS)
        words = [secretPassword]

        while len(words) < 3:
            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 0:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 5:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) == 3:
                words.append(randomWord)

        for b in range(500):
            if len(words) == 12:
                break

            randomWord = getOneWordExcept(words)
            if numMatchingLetters(secretPassword, randomWord) != 0:
                words.append(randomWord)

        while len(words) < 12:
            randomWord = getOneWordExcept(words)
            words.append(randomWord)

        assert len(words) == 12
        return words

    def getOneWordExcept(blocklist=None):
        if blocklist is None:
            blocklist = []

        while True:
            randomWord = random.choice(WORDS)
            if randomWord not in blocklist:
                return randomWord

    def numMatchingLetters(word1, word2):
        matches = 0
        for a in range(len(word1)):
            if word1[a] == word2[a]:
                matches += 1
            return matches

    def getComputerMemoryString(words):
        linesWithWords = random.sample(range(16 * 2), len(words))
        memoryAddress = 16 * random.randint(0, 4000)

        computerMemory = []
        nextWord = 0
        for lineNum in range(16):
            leftHalf = ''
            rightHalf = ''
            for j in range(16):
                leftHalf += random.choice(var_RobCo.GARBAGE_CHARS)
                rightHalf += random.choice(var_RobCo.GARBAGE_CHARS)

            if lineNum in linesWithWords:
                insertionIndex = random.randint(0, 9)
                leftHalf = (leftHalf[:insertionIndex] + words[nextWord] + leftHalf[insertionIndex + 7:])
                nextWord += 1

            if lineNum + 16 in linesWithWords:
                insertionIndex = random.randint(0, 9)
                rightHalf = (rightHalf[:insertionIndex] + words[nextWord] + rightHalf[insertionIndex + 7:])
                nextWord += 1

            computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                                  + '  ' + leftHalf + '    '
                                  + '0x' + hex(memoryAddress + (16 * 16))[2:].zfill(4)
                                  + '  ' + rightHalf)

            memoryAddress += 16

        return '\n'.join(computerMemory)

    def askForPlayerGuess(words, tries):
        while True:
            cmd_RobCo.char('\nEnter password: ({} tries remaining)'.format(tries))
            guess = input('> ').upper()
            if guess in words:
                return guess
            cmd_RobCo.char('That is not one of the possible passwords listed above')
            cmd_RobCo.char('Try entering "{}" or "{}".'.format(words[0], words[1]))

    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            sys.exit()
