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

from approvalratingsapp.models.services.demography_type_record import DemographyTypeRecordService
from approvalratingsapp.models.services.demography_record import DemographyRecordService

from ..models import (
    UserType,
    DemographyType,
    Demography,
    DemographyMapping,
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

    adminUserType = UserType("admin")
    raterUserType = UserType("rater")
    schoolDemoType = DemographyType("institution")
    yearDemoType = DemographyType("year")
    degDemoType = DemographyType("degree")
    classDemoType = DemographyType("class")
    subjectDemoType = DemographyType("subject")
    optsubjectDemoType = DemographyType("optional subject")
    optlanguageDemoType = DemographyType("optional language")
    with transaction.manager:
        DBSession.add(adminUserType)
        DBSession.add(raterUserType)

        DBSession.add(schoolDemoType)
        DBSession.flush()
        schoolDemoTypeID = schoolDemoType.id
        print "School Demography Type ID: ", schoolDemoTypeID
        xaviersDemo = Demography("St. Xavier's College", schoolDemoTypeID, "Xavier's")
        DBSession.add(xaviersDemo)
        DBSession.flush()
        xaviersDemoID = xaviersDemo.id

        yearDemoTypeID = DBSession.add(yearDemoType)
        yearDemoTypeID = DemographyTypeRecordService.by_demography_type(yearDemoType.demography_type).id
        print "Year Demography Type ID: ", yearDemoTypeID
        fyjcDemo = Demography("First Year Junior College", yearDemoTypeID, "FYJC")
        syjcDemo = Demography("Second Year Junior College", yearDemoTypeID, "SYJC")
        fydcDemo = Demography("First Year Degree College", yearDemoTypeID, "FY")
        sydcDemo = Demography("Second Year Degree College", yearDemoTypeID, "SY")
        tydcDemo = Demography("Third Year Degree College", yearDemoTypeID, "TY")
        
        DBSession.add(fyjcDemo)
        DBSession.flush()
        fyjcID = fyjcDemo.id
        DBSession.add(DemographyMapping(xaviersDemoID, fyjcID))
        
        DBSession.add(syjcDemo)
        DBSession.flush()
        syjcID = syjcDemo.id
        DBSession.add(DemographyMapping(xaviersDemoID, syjcID))
        
        DBSession.add(fydcDemo)
        DBSession.flush()
        fydcID = fydcDemo.id
        DBSession.add(DemographyMapping(xaviersDemoID, fydcID))
        
        DBSession.add(sydcDemo)
        DBSession.flush()
        sydcID = sydcDemo.id
        DBSession.add(DemographyMapping(xaviersDemoID, sydcID))
        
        DBSession.add(tydcDemo)
        DBSession.flush()
        tydcID = tydcDemo.id
        DBSession.add(DemographyMapping(xaviersDemoID, tydcID))


        degDemoTypeID = DBSession.add(degDemoType)
        degDemoTypeID = DemographyTypeRecordService.by_demography_type(degDemoType.demography_type).id
        baDemo = Demography("Bachelor of Arts", degDemoTypeID, "B.A.")
        bmmDemo = Demography("Bachelor of Mass Media", degDemoTypeID, "B.M.M.")
        bscDemo = Demography("Bachelor of Science", degDemoTypeID, "B.Sc.")
        bmsDemo = Demography("Bachelor of Management Studies", degDemoTypeID, "B.M.S.")
        bcomDemo = Demography("Bachelor of Commerce", degDemoTypeID, "B.COM")
        bscitDemo = Demography("Bachelor of Science Information Technology", degDemoTypeID, "B.Sc.I.T.")
        bvsdDemo = Demography("Bachelor of Vocation in Software Development", degDemoTypeID, "VOC.SOFT.")
        bvtDemo = Demography("Bachelor of Vocation in Tourism", degDemoTypeID, "VOC.TOUR.")
        bmmaDemo = Demography("Bachelor of Mass Media (Advertising)", degDemoTypeID, "B.M.M.(A.)")
        bmmjDemo = Demography("Bachelor of Mass Media (Journalism)", degDemoTypeID, "B.M.M.(J.)")
        hscaDemo = Demography("Higher Secondary Certificate (Arts)", degDemoTypeID, "H.S.C.(A.)")
        hscsDemo = Demography("Higher Secondary Certificate (Science)", degDemoTypeID, "H.S.C.(S.)")
        
        DBSession.add(baDemo)
        DBSession.flush()
        baID = baDemo.id
        DBSession.add(DemographyMapping(fydcID, baID))
        DBSession.add(DemographyMapping(sydcID, baID))
        DBSession.add(DemographyMapping(tydcID, baID))

        # BMM only for first two years
        DBSession.add(bmmDemo)
        DBSession.flush()
        bmmID = bmmDemo.id
        DBSession.add(DemographyMapping(fydcID, bmmID))
        DBSession.add(DemographyMapping(sydcID, bmmID))

        # Have to choose between Advertising and Journalism in third year 
        DBSession.add(bmmaDemo)
        DBSession.flush()
        bmmaID = bmmaDemo.id
        DBSession.add(DemographyMapping(tydcID, bmmaID))

        DBSession.add(bmmjDemo)
        DBSession.flush()
        bmmjID = bmmjDemo.id
        DBSession.add(DemographyMapping(tydcID, bmmjID))

        DBSession.add(bscDemo)
        DBSession.flush()
        bscID = bscDemo.id
        DBSession.add(DemographyMapping(fydcID, bscID))
        DBSession.add(DemographyMapping(sydcID, bscID))
        DBSession.add(DemographyMapping(tydcID, bscID))

        DBSession.add(bmsDemo)
        DBSession.flush()
        bmsID = bmsDemo.id
        DBSession.add(DemographyMapping(fydcID, bmsID))
        DBSession.add(DemographyMapping(sydcID, bmsID))
        DBSession.add(DemographyMapping(tydcID, bmsID))

        DBSession.add(bcomDemo)
        DBSession.flush()
        bcomID = bcomDemo.id
        DBSession.add(DemographyMapping(fydcID, bcomID))
        DBSession.add(DemographyMapping(sydcID, bcomID))
        DBSession.add(DemographyMapping(tydcID, bcomID))

        DBSession.add(bscitDemo)
        DBSession.flush()
        bscitID = bscitDemo.id
        DBSession.add(DemographyMapping(fydcID, bscitID))
        DBSession.add(DemographyMapping(sydcID, bscitID))
        DBSession.add(DemographyMapping(tydcID, bscitID))

        DBSession.add(bvsdDemo)
        DBSession.flush()
        bvsdID = bvsdDemo.id
        DBSession.add(DemographyMapping(fydcID, bvsdID))
        DBSession.add(DemographyMapping(sydcID, bvsdID))
        DBSession.add(DemographyMapping(tydcID, bvsdID))

        DBSession.add(bvtDemo)
        DBSession.flush()
        bvtID = bvtDemo.id
        DBSession.add(DemographyMapping(fydcID, bvtID))
        DBSession.add(DemographyMapping(sydcID, bvtID))
        DBSession.add(DemographyMapping(tydcID, bvtID))

        DBSession.add(hscaDemo)
        DBSession.flush()
        hscaID = hscaDemo.id
        DBSession.add(DemographyMapping(fyjcID, hscaID))
        DBSession.add(DemographyMapping(syjcID, hscaID))

        DBSession.add(hscsDemo)
        DBSession.flush()
        hscsID = hscsDemo.id
        DBSession.add(DemographyMapping(fyjcID, hscsID))
        DBSession.add(DemographyMapping(syjcID, hscsID))

        DBSession.add(classDemoType)
        DBSession.flush()
        classDemoTypeID = classDemoType.id
        groupA = Demography("Group A", classDemoTypeID)
        groupB = Demography("Group B", classDemoTypeID)
        groupC = Demography("Group C", classDemoTypeID)
        groupSci = Demography("Science", classDemoTypeID)
        
        DBSession.add(groupA)
        DBSession.flush()
        groupAID = groupA.id
        DBSession.add(DemographyMapping(hscaID, groupAID))

        DBSession.add(groupB)
        DBSession.flush()
        groupBID = groupB.id
        DBSession.add(DemographyMapping(hscaID, groupBID))

        DBSession.add(groupC)
        DBSession.flush()
        groupCID = groupC.id
        DBSession.add(DemographyMapping(hscaID, groupCID))

        DBSession.add(groupSci)
        DBSession.flush()
        groupSciID = groupSci.id
        DBSession.add(DemographyMapping(hscsID, groupSciID))

        DBSession.add(subjectDemoType)
        DBSession.flush()
        subjectDemoTypeID = subjectDemoType.id
        
        englishDemo = Demography("English", subjectDemoTypeID)
        DBSession.add(englishDemo)
        DBSession.flush()
        englishID = englishDemo.id
        DBSession.add(DemographyMapping(groupAID, englishID))
        DBSession.add(DemographyMapping(groupBID, englishID))
        DBSession.add(DemographyMapping(groupCID, englishID))
        DBSession.add(DemographyMapping(groupSciID, englishID))

        economicsDemo = Demography("Economics", subjectDemoTypeID)
        DBSession.add(economicsDemo)
        DBSession.flush()
        economicsID = economicsDemo.id
        DBSession.add(DemographyMapping(groupAID, economicsID))
        DBSession.add(DemographyMapping(groupBID, economicsID))
        DBSession.add(DemographyMapping(groupCID, economicsID))

        sociologyDemo = Demography("Sociology", subjectDemoTypeID)
        DBSession.add(sociologyDemo)
        DBSession.flush()
        sociologyID = sociologyDemo.id
        DBSession.add(DemographyMapping(groupAID, sociologyID))
        DBSession.add(DemographyMapping(groupCID, sociologyID))

        pyshcologyDemo = Demography("Psychology", subjectDemoTypeID)
        DBSession.add(pyshcologyDemo)
        DBSession.flush()
        psychologyID = pyshcologyDemo.id
        DBSession.add(DemographyMapping(groupAID, psychologyID))
        DBSession.add(DemographyMapping(groupBID, psychologyID))

        historyDemo = Demography("History", subjectDemoTypeID)
        DBSession.add(historyDemo)
        DBSession.flush()
        historyID = historyDemo.id
        DBSession.add(DemographyMapping(groupAID, historyID))
        DBSession.add(DemographyMapping(groupCID, historyID))

        mathsDemo = Demography("Mathematics", subjectDemoTypeID)
        DBSession.add(mathsDemo)
        DBSession.flush()
        mathsID = mathsDemo.id
        DBSession.add(DemographyMapping(groupBID, mathsID))
        DBSession.add(DemographyMapping(groupSciID, mathsID))

        politicsDemo = Demography("Politics", subjectDemoTypeID)
        DBSession.add(politicsDemo)
        DBSession.flush()
        politicsID = politicsDemo.id
        DBSession.add(DemographyMapping(groupBID, politicsID))
        DBSession.add(DemographyMapping(groupCID, politicsID))

        EVEDemo = Demography("Environment Education", subjectDemoTypeID, "EVE")
        DBSession.add(EVEDemo)
        DBSession.flush()
        EVEID = EVEDemo.id
        DBSession.add(DemographyMapping(groupAID, EVEID))
        DBSession.add(DemographyMapping(groupBID, EVEID))
        DBSession.add(DemographyMapping(groupCID, EVEID))
        DBSession.add(DemographyMapping(groupSciID, EVEID))

        phyisicsDemo = Demography("Physics", subjectDemoTypeID)
        DBSession.add(phyisicsDemo)
        DBSession.flush()
        physicsID = phyisicsDemo.id
        chemistryDemo = Demography("Chemistry", subjectDemoTypeID)


        DBSession.add(optsubjectDemoType)
        DBSession.flush()
        optsubjectDemoTypeID = optsubjectDemoType.id

        DBSession.add(optlanguageDemoType)
        DBSession.flush()
        optlanguageDemoTypeID = optlanguageDemoType.id

        hindiDemo = Demography("Hindi", optlanguageDemoTypeID)
        marathiDemo = Demography("Marathi", optlanguageDemoTypeID)
        frenchDemo = Demography("French", optlanguageDemoTypeID)
        itDemo = Demography("Information Technology", optlanguageDemoTypeID, "I.T.")
        bioDemo = Demography("Biology", optsubjectDemoTypeID, "Bio")
        geoDemo = Demography("Geology", optsubjectDemoTypeID, "Geo")
        econDemo = Demography("Economics (Option)", optsubjectDemoTypeID, "Eco")
        
        DBSession.add(hindiDemo)
        DBSession.flush()
        hindiDemoID = hindiDemo.id
        DBSession.add(DemographyMapping(groupAID, hindiDemoID))
        DBSession.add(DemographyMapping(groupBID, hindiDemoID))
        DBSession.add(DemographyMapping(groupCID, hindiDemoID))
        DBSession.add(DemographyMapping(groupSciID, hindiDemoID))
        
        DBSession.add(marathiDemo)
        DBSession.flush()
        marathiDemoID = marathiDemo.id
        DBSession.add(DemographyMapping(groupAID, marathiDemoID))
        DBSession.add(DemographyMapping(groupBID, marathiDemoID))
        DBSession.add(DemographyMapping(groupCID, marathiDemoID))
        
        DBSession.add(frenchDemo)
        DBSession.flush()
        frenchDemoID = frenchDemo.id
        DBSession.add(DemographyMapping(groupAID, frenchDemoID))
        DBSession.add(DemographyMapping(groupBID, frenchDemoID))
        DBSession.add(DemographyMapping(groupCID, frenchDemoID))
        DBSession.add(DemographyMapping(groupSciID, frenchDemoID))

        DBSession.add(itDemo)
        DBSession.flush()
        itDemoID = itDemo.id
        DBSession.add(DemographyMapping(groupAID, frenchDemoID))
        DBSession.add(DemographyMapping(groupBID, frenchDemoID))
        DBSession.add(DemographyMapping(groupCID, frenchDemoID))
        DBSession.add(DemographyMapping(groupSciID, frenchDemoID))

        DBSession.add(bioDemo)
        DBSession.flush()
        bioDemoID = bioDemo.id
        DBSession.add(DemographyMapping(groupSciID, bioDemoID))

        DBSession.add(geoDemo)
        DBSession.flush()
        geoDemoID = geoDemo.id
        DBSession.add(DemographyMapping(groupSciID, geoDemoID))
        
        DBSession.add(econDemo)
        DBSession.flush()
        econDemoID = econDemo.id
        DBSession.add(DemographyMapping(groupSciID, econDemoID))