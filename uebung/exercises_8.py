from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke

blatt8_1 = [
    [MultipleChoice("Welche Satzteile sind Nebensätze?", correct=["als sie ...", "damit sie ..."], wrong=["putzte er ..."])],
    [SelectionList("Um was für einen Satz handelt es sich syntaktisch bei <i>als sie ...</i>?", "Adverbialsatz", "Komplementsatz", "Attributsatz", "Matrixsatz", inst=selection)],
    [SelectionList("Was ist <i>als sie ...</i> semantisch für ein Satz?", "Temporalsatz", "Finalsatz", "Relativsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", inst=selection)],
    [MultipleChoice("Welche Aussagen stimmen für den Teilsatz <i>als sie ...</i> formal gesehen?", correct=["Konjunktionalsatz", "Nebensatz 1. Grades", "Vordersatz"], wrong=["Nachsatz", "Nebensatz 2. Grades"])],
    [SelectionList("Um was für einen Satz handelt es sich syntaktisch bei <i>damit sie ...</i>?", "Adverbialsatz", "Komplementsatz", "Attributsatz", "Matrixsatz", inst=selection)],
    [SelectionList("Was ist <i>damit sie ...</i> semantisch für ein Satz?", "Finalsatz", "Temporalsatz", "Relativsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", inst=selection)],
    [MultipleChoice("Welche Aussagen stimmen für den Teilsatz <i>damit sie ...</i> formal gesehen?", correct=["Konjunktionalsatz", "Nebensatz 1. Grades", "Nachsatz"], wrong=["Vordersatz", "Nebensatz 2. Grades"])]
] 

blatt8_2a = [
    [MultipleChoice("Welche Wörter stehen im Vorfeld?", correct=["Der", "kleine", "Junge"], wrong=["Das Vorfeld ist unbesetzt.", "hat", "heute", "das", "Buch", "gelesen"])],
    [MultipleChoice("Welche Wörter sind Teil der linken Satzklammer?", correct=["hat"], wrong=["Die linke SK ist unbesetzt.", "der", "kleine", "Junge", "heute", "das", "Buch", "gelesen"])],
    [MultipleChoice("Welche Wörter stehen im Mittelfeld?", correct=["heute", "das", "Buch"], wrong=["Das Mittelfeld ist unbesetzt.", "hat", "Der", "kleine", "Junge", "gelesen"])],
    [MultipleChoice("Welche Wörter sind Teil der rechten Satzklammer?", correct=["gelesen"], wrong=["Die rechte SK ist unbesetzt.", "der", "kleine", "Junge", "heute", "das", "Buch", "hat"])],
    [SingleChoice("Welche Aussage über das Nachfeld des Hauptsatzes ist korrekt?", "Der Nebensatz steht im Nachfeld.", "Das Nachfeld ist unbesetzt.", sonst=False)],
]


blatt8_2b = [
    [MultipleChoice("Welche Wörter stehen im Vorfeld?", correct=["Das Vorfeld ist unbesetzt."], wrong=["das", "ihm", "sein", "Vater", "zu", "Weihnachten", "schenkte"])],
    [MultipleChoice("Welche Wörter sind Teil der linken Satzklammer?", correct=["das"], wrong=["Die linke SK ist unbesetzt.", "ihm", "sein", "Vater", "zu", "Weihnachten", "schenkte"])],    
    [MultipleChoice("Welche Wörter stehen im Mittelfeld?", correct=["ihm", "sein", "Vater", "zu", "Weihnachten"], wrong=["Das Mittelfeld ist unbesetzt.", "das", "schenkte"])],
    [MultipleChoice("Welche Wörter sind Teil der rechten Satzklammer?", correct=["schenkte"], wrong=["Die rechte SK ist unbesetzt.", "ihm", "sein", "Vater", "zu", "Weihnachten", "das"])]  
]

blatt8_3 = [
    [MultipleChoice("Identifizieren Sie das Vorfeld des ersten und das Vorfeld des zweiten Satzes.", correct=["Peter gesungen", "Ein Lied gesungen"], wrong=["Peter", "Ein Lied", "Ein", "gesungen", "Peter gesungen hat", "Ein Lied gesungen hat", "Lied gesungen"])],
    [MultipleChoice("Wann ist die Konstituentenverbindung <i>Satzglied + infinites Verb</i> im Vorfeld inakzeptabel?", correct=["Wenn es sich bei dem Satzglied um das Subjekt handelt."], wrong=["Wenn es sich bei dem Satzglied um das Objekt handelt."], inst=single)],
    [SingleChoice("Welche übergeordnete Konstituente läßt sich im Fall des erfolgreichen Permutationstests durch gemeinsame Verschiebung ins Vorfeld feststellen?", "VP", "S-bar", "ccomp", "aux", sonst=False)],
]

blatt8_4 = [
    [SingleChoice("'Präpositionale Objekte stehen in Verbendsätzen in der Regel unmittelbar vor dem finiten Verb.'", "Satz 1", "Satz 2", "Satz 3", "Satz 4", sonst=False)],
    [SingleChoice("'Die Abfolgeregularität für Personalpronomina ist normalerweise ›Subjekt vor Akkusativobjekt vor Dativobjekt‹.'", "Satz 3", "Satz 1", "Satz 2", "Satz 4", sonst=False)],
    [SingleChoice("'Im unmarkierten Fall steht die Modalpartikel an der linken Peripherie des Mittelfelds (Wackernagel-Position).'", "Satz 4", "Satz 1", "Satz 2", "Satz 3", sonst=False)],
    [SingleChoice("'Die (markierte) Abfolge ›Subjekt vor Akkusativobjekt vor Dativobjekt‹ für nominale Satzglieder ist nur möglich, wenn bestimmte Bedingungen erfüllt sind (insbesondere Thema vor Rhema).'", "Satz 2", "Satz 1", "Satz 3", "Satz 4", sonst=False)],
]



#Objektsatz
blatt8_5a = [
    [SingleChoice("Was für eine Satzkonstruktion liegt hier vor?", "subordiniert", "koordiniert", sonst=True)],
    [SelectionList("Welcher eingebettete Satztyp liegt vor?", "Objektsatz", "Subjektsatz", "Relativsatz", "Temporalsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", sonst=True, inst=selection)],
    [SelectionList("Wie läßt sich dieser Satztyp klassifizieren?", "Komplementsatz", "Attributsatz", "Adverbialsatz", "Matrixsatz", sonst=False, inst=selection)],    
    ]


#Infinitiv-Komplementsatz
blatt8_5b = [
    [SingleChoice("Was für eine Satzkonstruktion liegt hier vor?", "subordiniert", "koordiniert", sonst=True)],
    [SelectionList("Welcher eingebettete Satztyp liegt vor?", "Infinitiv-Objektsatz", "Subjektsatz", "Relativsatz","Temporalsatz", "Kausalsatz", "Modalsatz", "Lokalsatz",  sonst=True, inst=selection)],
    [SelectionList("Wie läßt sich dieser Satztyp klassifizieren?", "Komplementsatz", "Attributsatz", "Adverbialsatz","Matrixsatz",  sonst=False, inst=selection)],    
    ]

blatt8_5b_zusatz = [
    [SingleChoice("Welche Form der Kontrolle liegt hier vor?", "Subjektkontrolle", "Objektkontrolle")],
    [SingleChoice("Welche Form der Kontrolle liegt in folgendem Satz vor: <i>Sie überreden ihn, nach München zu fahren</i>?", "Objektkontrolle", "Subjektkontrolle")],
    [MultipleChoice("Welche satzwertigen Funktionen können Infinitivkonstruktionen erfüllen?", correct=["Komplementsatz (<code>xcomp</code>)", "Attributsatz (<code>acl</code>)", "Adverbialsatz (<code>advcl</code>)"], wrong=["Relativsatz"])]
    ]


#Relativsatz
blatt8_5c = [
    [SingleChoice("Was für eine Satzkonstruktion liegt hier vor?", "subordiniert", "koordiniert", sonst=True)],
    [SelectionList("Welcher eingebettete Satztyp liegt vor?", "Relativsatz", "Objektsatz", "Subjektsatz", "Temporalsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", sonst=True, inst=selection)],
    [SelectionList("Wie läßt sich dieser Satztyp klassifizieren?", "Attributsatz", "Komplementsatz", "Adverbialsatz","Matrixsatz",  sonst=False, inst=selection)],    
    ]

blatt8_5c_zusatz = [
    [MultipleChoice("Welche Attributsatztypen haben Sie in der Vorlesung kennengelernt?", correct=["adnominaler Substantivsatz: <i>die Frage, wie ... </i>", "satzwertiger Nominalmodifikator (<code>acl</code>): <i>der amtierende Präsident</i>", "Relativsatz (<code>acl:relcl</code>)"], wrong=["Adverbialsatz: <i>er tanzte, bis ...</i>"])]
    ]


#Satz-Koordination
blatt8_5d = [
    [SingleChoice("Was für eine Satzkonstruktion liegt hier vor?", "koordiniert", "subordiniert", sonst=True)],
    [SelectionList("Welcher eingebettete Satztyp liegt vor?", "Keine der Alternativen", "Objektsatz", "Subjektsatz", "Relativsatz", "Temporalsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", sonst=False, inst=selection)],
    [SelectionList("Welcher Satztyp kommt vor?", "Hauptsatz", "Matrixsatz", "Komplementsatz", "Attributsatz", "Adverbialsatz", sonst=True, inst=selection)],
    ]


#komplexe VP
blatt8_5e = [
    [SingleChoice("Was für eine Satzkonstruktion liegt hier vor?", "Keine der anderen Möglichkeiten", "koordiniert", "subordiniert")],
    [SelectionList("Welche eingebettete Satztyp liegt vor?", "Keine der Alternativen",  "Objektsatz", "Subjektsatz", "Relativsatz", "Temporalsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", inst=selection)],
    [SelectionList("Wie läßt sich dieser Satztyp klassifizieren?", "Satz mit komplexer VP", "Matrixsatz", "Komplementsatz", "Attributsatz", "Adverbialsatz", sonst=False, inst=selection)],
    ]


#Adverbialsatz
blatt8_5f = [
    [SingleChoice("Was für eine Satzkonstruktion liegt hier vor?", "subordiniert", "koordiniert", sonst=True)],
    [SelectionList("Welcher eingebettete Satztyp liegt vor?", "Temporalsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", "Objektsatz", "Subjektsatz", "Relativsatz", sonst=True, inst=selection)],
    [SelectionList("Wie läßt sich dieser Satztyp klassifizieren?", "Adverbialsatz", "Komplementsatz", "Attributsatz", "Matrixsatz", sonst=False, inst=selection)],    
    ]


#Infinitiv-Subjektsatz
blatt8_5g = [
    [SingleChoice("Was für eine Satzkonstruktion liegt hier vor?", "subordiniert", "koordiniert", sonst=True)],
    [SelectionList("Welcher eingebettete Satztyp liegt vor?", "Infinitiv-Subjektsatz", "Objektsatz", "Relativsatz", "Temporalsatz", "Kausalsatz", "Modalsatz", "Lokalsatz", sonst=True, inst=selection)],
    [SelectionList("Wie läßt sich dieser Satztyp klassifizieren?", "Komplementsatz", "Attributsatz", "Adverbialsatz", "Matrixsatz",  sonst=False, inst=selection)],    
    ]

blatt8_6 = [
    [SingleChoice("Um welche Satzart handelt es sich bei Satz 1?", "Aussagesatz", "Fragesatz", "Aufforderungssatz", "Wunschsatz")],
    [MultipleChoice("Wieso?", correct=["Verbzweitstellung", "Modus: Indikativ", "Satzschlusszeichen: Punkt"], wrong=["Fragepronomen", "steigende Intonation", "Satzschlusszeichen: Fragezeichen", "Es handelt sich kommunikativ um eine Aufforderung."])],
    [SingleChoice("Um welche Satzart handelt es sich bei Satz 2?", "Fragesatz", "Aussagesatz", "Aufforderungssatz", "Wunschsatz")],
    [MultipleChoice("Wieso?", wrong=["Verbzweitstellung", "Modus: Indikativ", "Satzschlusszeichen: Punkt", "Es handelt sich kommunikativ um eine Aufforderung."], correct=["Fragepronomen", "steigende Intonation", "Satzschlusszeichen: Fragezeichen"])],
    [SingleChoice("Um welche Satzart handelt es sich bei Satz 3?", "Aussagesatz", "Fragesatz", "Aufforderungssatz", "Wunschsatz")],
    [MultipleChoice("Wieso?", correct=["Verbzweitstellung", "Modus: Indikativ", "Satzschlusszeichen: Punkt"], wrong=["Fragepronomen", "steigende Intonation", "Satzschlusszeichen: Fragezeichen", "Es handelt sich kommunikativ um eine Aufforderung."])]
]

blatt8_7 = [
    [MultipleChoice("Wenn der Nebensatz durch eine Konjunktion eingeleitet wird, wo steht diese im Stellungsfeldermodell?", correct=["linke Satzklammer"], wrong=["Nachfeld", "rechte Satzklammer", "Vorfeld", "Mittelfeld"])],
    [SingleChoice("Von welchem Satzteil wird diese Position gefüllt, wenn die Konjunktion fehlt?","finites Verb", "Subjekt", "infinites Verb", "Objekt", "Adverb", "Adjektiv")],
    [MultipleChoice("Kann diese Position theoretisch auch leer bleiben?", correct=["Nein, der Satz wird dann ungrammatisch."], wrong=["Ja, der Satz bleibt unverändert grammatisch."])]
]
