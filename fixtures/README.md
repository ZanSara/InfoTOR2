# Come creare un dump

Dalla macchina locale:
`python manage.py dumpdata --natural-foreign --natural-primary > fixtures/dumpdata.json`
(le flag `natural` potrebbero non essere necessarie)

Pushare tutto e in remoto eseguire

`python manage.py loaddata fixtures/dumpdata.json`

In caso di errori, fixarli manualmente nel json e eventualmente reimportare anche nel db di sviluppo locale.
