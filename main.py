# -*- coding: utf-8 -*-

WORDLIST_FILENAME = 'words-utf8.txt'
HEBREW_WORDS = [w.split()[0] for w in file(WORDLIST_FILENAME, 'r').readlines()]
KALPI_WORDS = ['אמת', 'זך', 'ףץ', 'ל', "נז", "ג", "יז", "י", "יץ", "רק", "מחל", "קץ", "שס", "קנ", "ף", "ני", "ודעם", "פה", "כ", "זץ", "נץ", "מרצ", "ע", "טב", "ז"]

def initial_form(w):
    w = w.replace('ף', 'פ')
    w = w.replace('ץ', 'צ')
    w = w.replace('ן', 'נ')
    w = w.replace('ם', 'מ')
    w = w.replace('ך', 'כ')
    return w

KALPI_INITIAL = [initial_form(w) for w in KALPI_WORDS]

def process():
    to_process = [('', w) for w in HEBREW_WORDS]
    done = []

    while to_process:
        current_process = to_process
        to_process = []

        for beginning, remaining in current_process:
            for kalpi in KALPI_WORDS:
                if remaining == kalpi:
                    done.append(beginning + remaining)
                elif remaining.startswith(kalpi):
                    to_process.append((beginning + kalpi, remaining[len(kalpi):]))

    return sorted(set(done))

def process_allow_finals():
    to_process = [('', w) for w in HEBREW_WORDS]
    done = []

    while to_process:
        current_process = to_process
        to_process = []

        for beginning, remaining in current_process:
            for kalpi in KALPI_INITIAL:
                if initial_form(remaining) == kalpi:
                    done.append(beginning + remaining)
                elif initial_form(remaining).startswith(kalpi):
                    to_process.append((beginning + remaining[:len(kalpi)], remaining[len(kalpi):]))

    return sorted(set(done))