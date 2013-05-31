#!/bin/sh
logreopen=${VARPATH}/narrative.logreopen
if [ ! -e "$logreopen" ]; then
  touch $logreopen
fi

${ENVPATH}/python/bin/python ${ENVPATH}/python/bin/bake -m spire.tasks \
  spire.schema.deploy schema=narrative config=${SVCPATH}/narrative/narrative.yaml
ln -sf ${SVCPATH}/narrative/narrative.yaml ${CONFPATH}/uwsgi/narrative.yaml
