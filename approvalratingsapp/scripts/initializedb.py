import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import (
    DBSession,
    Base,
    )

from ..models import (
    UserType,
    RateeType,
    User,
    Ratee,
    UserRating,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        adminUserType = UserType("admin")
        DBSession.add(adminUserType)
        adminUserType = DBSession.query(UserType).filter_by(user_type="admin").first()
        rateeType = RateeType("celebrity")
        DBSession.add(rateeType)
        rateeType = DBSession.query(RateeType).filter_by(ratee_type="celebrity").first()
        ratee = Ratee("Narendra Modi", rateeType.id)
        DBSession.add(ratee)
        raterUserType = UserType("rater")
        DBSession.add(raterUserType)