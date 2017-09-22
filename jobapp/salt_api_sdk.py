# -*- encoding:utf-8 -*-
#--------------------------------
# @Date    : 2017-05-10 15:00
# @Author  : wye
# @Version : v1.0
# @Desrc   : salt api sdk interface
# -------------------------------- 

import salt.config
import salt.client
import salt.runner 



def get_keep_jobs_time():
    master_opts = salt.config.client_config('/etc/salt/master')
    keep_jobs_hours = master_opts['keep_jobs']
    return keep_jobs_hours/24



def get_running_jobs_info():
    master_opts = salt.config.client_config('/etc/salt/master')
    runner= salt.runner.RunnerClient(master_opts)
    resp = runner.cmd('jobs.active',print_event=False)
    return len(resp),resp



def get_host_meta_info(hostname):
    local = salt.client.LocalClient()
    resp = local.cmd(hostname,'grains.items')
    return resp[hostname]



def get_host_status(hostname):
    local = salt.client.LocalClient()
    resp = local.cmd(hostname,'test.ping',timeout=2)
    print resp
    if resp and resp[hostname]:
        return 1
    else:
        return 0


def get_hosts_status(hostnames_list):
    local = salt.client.LocalClient()
    resp = local.cmd(hostnames_list,'test.ping',expr_form='list',timeout=2)
    return resp


def init_sys_env(target_hosts_list):
    local = salt.client.LocalClient()
    resp = local.cmd_async(target_hosts_list,'state.sls',['test.init_env'],expr_form='list',timeout=2)
    print resp



def state_sls_job_execute_real(target_hosts_list,action):
    local = salt.client.LocalClient()
    if action == "initsys":
        jid = local.cmd_async(target_hosts_list,'state.sls',['test.init_env'],expr_form='list',timeout=2)
    return jid



def state_sls_job_execute_test(target_hosts_list,action):
    local = salt.client.LocalClient()
    if action == "initsys":
        jid = local.cmd_async(target_hosts_list,'state.sls',['test.init_env','test=true'],expr_form='list',timeout=2)
    return jid



def state_sls_execute(target_hosts_list,action,is_test):
    args = []

    if action == "initsys":
        args.append("initEnv.init")
    elif action == "install_jdk1760":
        args.append("jdk1760.init")
    elif action == "install_jdk1779":
        args.append("jdk1779.init")
    elif action == "install_jdk1874":
        args.append("jdk1874.init")
    elif action == "install_jdk18131":
        args.append("jdk18131.init")
    elif action == "install_tomcat7":
        args.append("tomcat7.init")
    elif action == "install_tomcat8":
        args.append("tomcat8.init")
    elif action == "install_nginx":
        args.append("tengine.init")
    elif action == "install_zabbix":
        args.append("zabbix.init")
    elif action == "install_redis":
        args.append("redis.init")
    elif action == "upgrade_ssh":
        args.append("openssl.init")

    if is_test != None:args.append("test=true")

    local = salt.client.LocalClient()
    jid = local.cmd_async(target_hosts_list,'state.sls',args,expr_form='list',timeout=2)
    return jid



def get_salt_group_hosts(GroupExpr):
    local = salt.client.LocalClient()
    resp = local.cmd(GroupExpr,'grains.items',expr_form='compound',timeout=2)
    return resp



def test():
    local = salt.client.LocalClient()
    resp = local.cmd('*','cp.get_file',['salt://test.txt','/tmp/zxczxcz/test.txt','makedirs=true','gzip=5'],timeout=2)
    return  resp



def test1():
    local = salt.client.LocalClient()
    resp = local.cmd('*','cp.get_url',['http://172.29.19.13/PatchForCentos_V1.4.zip','/tmp/zxczxcz123/test.zip','makedirs=true'],timeout=2)
    return  resp



def cmd_run_job_execute_real(target_hosts_list,cmd):
    local = salt.client.LocalClient()
    jid = local.cmd_async(target_hosts_list,'cmd.run',[cmd],expr_form='list',timeout=2)
    return jid



def cmd_run_job_execute_test(target_hosts_list,cmd):
    local = salt.client.LocalClient()
    jid = local.cmd_async(target_hosts_list,'cmd.run',[cmd,'test=true'],expr_form='list',timeout=2)
    return jid


def upload_file(target_hosts_list,user,source_file_name,dest_file_path):
    local = salt.client.LocalClient()
    jid = local.cmd_async(target_hosts_list,'cp.get_file',['salt://%s/%s'%(user,source_file_name),dest_file_path,'makedirs=true','gzip=5'],expr_form='list',timeout=2)
    return  jid


def get_file_stats(host,file_path):
    local = salt.client.LocalClient()
    resp = local.cmd(host,'file.stats',[file_path],timeout=2)
    return resp



if __name__ == "__main__":

    # # obtain keep_jobs
    # import salt.config
    # master_opts = salt.config.client_config('/etc/salt/master')
    # print master_opts['keep_jobs']

    # # salt client interface,execute salt cli cmd.
    import salt.client
    local = salt.client.LocalClient()
    resp = local.cmd('*','cmd.run',["whoami && pwd"],kwarg={'runas':'securityadmin'})
    print resp

    # # execute salt cli async cmd
    # import salt.client
    # local = salt.client.LocalClient()
    # resp = local.cmd_async('*','cmd.run',['sleep 10;hostname'])
    # print resp

    # # execute salt cli async cmd
    # import salt.client
    # local = salt.client.LocalClient()
    # resp = local.cmd_async('*','cmd.run',['sleep 13;hostname'])
    # print resp

    # # saltutil.find_job
    # # import salt.client
    # # local = salt.client.LocalClient()
    # # resp = local.cmd('*','saltutil.find_job',['20170510152420651416'])
    # # print resp


    # # execute salt-run cli cmd
    # import salt.runner
    # runner1 = salt.runner.RunnerClient(master_opts)
    # resp = runner1.cmd('jobs.active',print_event=False)
    # print len(resp)

    #print get_host_meta_info("W612-JENKDOCK-3")
    #print get_host_status("BGP-NETAM-01")
    #init_sys_env(["W612-JENKDOCK-3","W612-JENKDOCK-4"])
    #print get_salt_group_hosts("S@172.16.4.136")
    #print test1()
    #print get_file_stats("W612-JENKDOCK-3","/tmp/test.txt")
    pass
