# -*- coding: utf-8 -*-

from scan import complaints
from scan import download

#download.getOldDecisions()

complaints = complaints.complaints(quick = True)
#import profile
#profile.run('complaints.getAll()')
#complaints.getAll()
complaints.getOld()
complaints.getWWW()
complaints.getNZLII()
#complaints.getOthers()