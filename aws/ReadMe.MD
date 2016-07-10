### new instance can't ping
console->security groups
edit the 'dyno' security group, if don't find it, create one
actions->edit inbound rules
type='all traffic' source='anywhere/my id'
then you can ping the vps
