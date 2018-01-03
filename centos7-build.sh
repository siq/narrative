#!/bin/bash
interpolate() {
  perl -p -e 's/\$\{([^}]+)\}/defined $ENV{$1} ? $ENV{$1} : $&/eg; s/\$\{([^}]+)\}//eg' $1 > $2 
}

python setup.py install --no-compile --single-version-externally-managed --record=/dev/null --prefix=${BUILDPATH}/usr --install-lib=${BUILDPATH}/usr/lib/python2.7/site-packages --install-scripts=${BUILDPATH}${BINPATH}

interpolate pkg/narrative.yaml narrative.yaml.install
install -D -m 0644 narrative.yaml.install $BUILDPATH$SVCPATH/narrative/narrative.yaml

interpolate pkg/logrotate.conf logrotate.conf.install
install -D -m 0644 logrotate.conf.install $BUILDPATH/etc/logrotate.d/siq-narrative
