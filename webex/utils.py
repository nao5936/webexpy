COMMON_NS = 'http://www.webex.com/schemas/2002/06/common'
SERVICE_NS = 'http://www.webex.com/schemas/2002/06/service'

EP_NS = '%s/ep' % SERVICE_NS
EVENT_NS = '%s/event' % SERVICE_NS
ATTENDEE_NS = '%s/attendee' % SERVICE_NS
HISTORY_NS = '%s/history' % SERVICE_NS

def is_blank(s):
    return s is None or not s.strip()
