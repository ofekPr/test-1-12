# Here is my answer for an example test
15 נק') מומלץ להעתיק את קטע הקוד ל pycharm ולהשלים ולבדוק שם את קטע הקוד המבוקש.
אין חובה להוסיף תיעוד.
          המרת פועל לגוף שלישי יחיד באנגלית
פעלים בגוף שלישי יחיד באנגלית מאופיינים ע"י הוספת הסיומת s  לפועל המקורי.
לדוגמה:
run -> runs
ניתן להגדיר את סט הכללים הבא:
1.	אם הפועל מסתיים ב y, הורד את ה y והוסף ies (try -> tries)
2.	אם הפועל נסתיים ב o, ch, s, sh, x או z, הוסף סיומת es (brush->brushes)
3.	לכל השאר, פשוט הוסף s (climb->climbs)
השלימו את הפונקציה make_3sg_form(verb) אשר מקבלת פועל באנגלית ומחזירה את הפועל בגוף שלישי יחיד.
import sys

Y_END = 'y'
Y_END_SUFFIX = 'ies'
DOUBLE_END = ['sh', 'ch']
SINGLE_END = ['x', 's', 'o', 'z']
SPECIAL_SUFFIX = 'es'
REGULAR_SUFFIX = 's'


def make_3sg_form(verb):
    """
    returns the Third Person Singular form of the passed verb.
    :verb: the verb to manipulate
    :return: the verb in its Third Person Singular form
    """


2.	הוסיפו asserts לפונקציה שכתבתם (10 נק')

3.	קבלת פרמטרים לסקריפט (25 נקודות)

כיתבו סקריפט שמקבל כפרמטר שם של קובץ ומדפיס את התוכן שלו למסך.

4.	(25 נק') בתרגיל זה עליכם לכתוב פונקציה שמקבלת מחרוזת ומחזירה מחרוזת חדשה, שכוללת כל תו של המחרוזת המקורית פעמיים. עקב קיצוצים בתקציב אנחנו נדרשים לכתוב את כל הפונקציות שלנו בשורה אחת בלבד. זה אומר שאחרי ההגדרה של def ושם הפונקציה, צריכה להיכתב שורה אחת בלבד.

5.	(25 נק') הינכם מתכנתים מערכת לניהול כח אדם במפעל. 
-	יש להגדיר class בשם employee. לכל אובייקט מסוג employee יש שם, תעודת זהות ושכר חודשי. לדוגמה-
shlomit, 123456, 5000
-	הוסיפו מתודה לעדכון השכר של עובד מסויים. המתודה תפעל על אובייקט מסוג employee ותעדכן את המשכורת שלו.
-	צרו class מסוג manager, מנהל, אשר יורש מ-employee, אבל בנוסף מוגדר לו גם בונוס שנתי. לדוגמה- 
Tal, 222333, 8000, 60000 
