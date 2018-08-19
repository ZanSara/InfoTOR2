import dbf

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Converte file .dbf in .csv. Utilizzo: python manage.py managedbf <file1.dbf> [file2.dbf] [file3.dbf] [...]'

    def add_arguments(self, parser):
        parser.add_argument('file_dbf', nargs='+', type=str)

    def handle(self, *args, **options):
        for dbf_filename in options['file_dbf']:
        
            # Convert DBF into CSV: 
            # https://pythonhosted.org/dbf/
            # https://stackoverflow.com/questions/45948295/how-to-convert-dbf-to-csv
            # https://stackoverflow.com/questions/13944427/error-when-trying-to-convert-dbf-to-csv-in-python#13944926
            
            try:
                name_extension = dbf_filename.split(".")
                if name_extension[-1] != 'dbf':
                    self.stdout.write(self.style.ERROR('Il file {} non ha estensione .dbf e non è stato importato.'.format(dbf_filename)))
                    continue
                
                tablename = ".".join(name_extension[:-1])
                table = dbf.Table(dbf_filename)
                table.open()
                dbf.export(table, "{}.csv".format(tablename), header=True)
                
                self.stdout.write(self.style.SUCCESS("File '{}' convertito con successo.".format(dbf_filename)))
            
            except:
                self.stdout.write(self.style.ERROR("Si è verificato un errore nel convertire il file '{}'. Il file non è stato convertito.".format(dbf_filename)))
                
            
    #            try:
    #                poll = Poll.objects.get(pk=poll_id)
    #            except Poll.DoesNotExist:
    #                raise CommandError('Poll "%s" does not exist' % poll_id)

    #            poll.opened = False
    #            poll.save()

            
        # self.stdout.write(self.style.SUCCESS("Accedi alla pagina admin per verificare l'avvenuto import dei dati."))

