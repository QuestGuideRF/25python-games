import argparse
import os
import runpy
def game_file (name ):
    return (
    name .endswith ('.py')
    and not name .startswith ('__')
    and name !='utils.py'
    )
def main ():
    directory =os .path .dirname (os .path .realpath (__file__ ))
    contents =os .listdir (directory )
    games =sorted (name [:-3 ]for name in contents if game_file (name ))
    parser =argparse .ArgumentParser (
    prog ='freegames',
    description ='Бесплатные игры на Python',
    epilog ='© Грант Дженкс, 2023 г.',
    )
    subparsers =parser .add_subparsers (dest ='command',help ='подкоманда help')
    subparsers .required =True
    subparsers .add_parser ('list',help ='список игр')
    parser_play =subparsers .add_parser ('play',help ='играть в бесплатные игры на Python')
    parser_play .add_argument ('game',choices =games ,help ='название игры')
    parser_show =subparsers .add_parser ('show',help ='покажи исходный код игры')
    parser_show .add_argument ('game',choices =games ,help ='название игры')
    parser_copy =subparsers .add_parser ('copy',help ='скопировать исходный код игры')
    parser_copy .add_argument ('game',choices =games ,help ='название игры')
    parser_copy .add_argument (
    '--force',
    action ='store_true',
    help ='перезаписать существующий файл',
    )
    args =parser .parse_args ()
    if args .command =='list':
        for game in games :
            print (game )
    elif args .command =='play':
        runpy .run_module ('freegames.'+args .game )
    elif args .command =='show':
        with open (os .path .join (directory ,args .game +'.py'))as reader :
            print (reader .read ())
    else :
        assert args .command =='copy'
        filename =args .game +'.py'
        with open (os .path .join (directory ,filename ))as reader :
            text =reader .read ()
        cwd =os .getcwd ()
        path =os .path .join (cwd ,filename )
        if args .force or not os .path .exists (path ):
            with open (path ,'w')as writer :
                writer .write (text )
        else :
            print ('ОШИБКА: Файл уже существует. Укажите --force для перезаписи.')
if __name__ =='__main__':
    main ()