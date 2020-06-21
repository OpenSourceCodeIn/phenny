#!/usr/bin/python3
def invite(phenny, input):
    phenny.say('Inviting {}'.format(input.group(1)))
    phenny.proto.invite('#osci', input.group(1))

invite.commands = ['invite']
invite.priority = 'high'
