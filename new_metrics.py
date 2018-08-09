#!python3

import datetime
from sqlalchemy import *
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from new_graphs import failure_mode_graph_generator
from productionconfig import *


sql_string = sql_dialect+sql_username+sql_password+sql_host+sql_database
engine = create_engine(sql_string)
connection = engine.connect()


#WHERE synthesis_date > (current_date - interval '5' day);

#silanization_name ="SELECT DISTINCT bonding_and_silanization_failure_mode FROM jira_lims_chips WHERE bonding_and_silanization_failure_mode IS NOT NULL ORDER BY bonding_and_silanization_failure_mode"
#silanization_fail = "SELECT summary, status, bonding_and_silanization_failure_mode FROM jira_lims_chips WHERE status = 'Failed' AND bonding_and_silanization_failure_mode IS NOT NULL AND failed_bonding__silanization_date > (current_date - interval '10' day) ORDER BY bonding_and_silanization_failure_mode;"

#synthesis_name="SELECT DISTINCT synthesis_failure FROM jira_lims_chips WHERE synthesis_failure IS NOT NULL ORDER BY synthesis_failure"
#synthesis_fail="SELECT summarycolors = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] status, synthesis_failure FROM jira_lims_chips WHERE status = 'Failed' AND synthesis_failure IS NOT NULL ORDER BY synthesis_failure;"

#deprotection_name="SELECT DISTINCT deprotection_failure FROM jira_lims_chips WHERE deprotection_failure IS NOT NULL ORDER BY deprotection_failure"
#deprotection_fail="SELECT summary, status, deprotection_failure FROM jira_lims_chips WHERE status = 'Failed' AND deprotection_failure IS NOT NULL ORDER BY deprotection_failure;"

#hyb_qc_name="SELECT DISTINCT hyb_qc_failure FROM jira_lims_chips WHERE hyb_qc_failure IS NOT NULL ORDER BY hyb_qc_failure"
#hyb_qc_fail="SELECT summary, status, hyb_qc_failure FROM jira_lims_chips WHERE status = 'Failed' AND hyb_qc_failure IS NOT NULL ORDER BY hyb_qc_failure;"

sample_hyb_name="SELECT DISTINCT sample_hybridization_failure_mode FROM jira_lims_chips WHERE sample_hybridization_failure_mode IS NOT NULL ORDER BY sample_hybridization_failure_mode;"
sample_hyb_failures="SELECT summary, status, sample_hybridization_failure_mode FROM jira_lims_chips WHERE (status = 'Failed' OR status = 'Failure Analysis') AND sample_hybridization_failure_mode IS NOT NULL ORDER BY sample_hybridization_failure_mode;"

extension_name="SELECT DISTINCT failed_extension FROM jira_lims_chips WHERE failed_extension IS NOT NULL ORDER BY failed_extension"
extension_failures="SELECT summary, status, failed_extension FROM jira_lims_chips WHERE (status = 'Failed'OR status='Failure Analysis') AND failed_extension IS NOT NULL ORDER BY failed_extension;"

process_failure_name = "SELECT DISTINCT process_of_failure FROM jira_lims_chips WHERE process_of_failure IS NOT NULL ORDER BY process_of_failure;"
process_failure_failures = "SELECT summary, status, process_of_failure FROM jira_lims_chips WHERE (status = 'Failed'OR status='Failure Analysis') AND process_of_failure IS NOT NULL ORDER BY process_of_failure "

seven_day_completions = connection.execute("SELECT summary FROM jira_lims_chips WHERE flowcell_completion_date IS NOT NULL AND flowcell_completion_date > (current_date - interval '7' day);")
one_day_completions = connection.execute("SELECT summary FROM jira_lims_chips WHERE flowcell_completion_date IS NOT NULL AND flowcell_completion_date > (current_date - interval '1' day);")

#failure_mode_graph_generator(silanization_name,silanization_fail,connection)
#failure_mode_graph_generator(synthesis_name,synthesis_fail,connection)
#failure_mode_graph_generator(deprotection_name,deprotection_fail,connection)
#failure_mode_graph_generator(hyb_qc_name,hyb_qc_fail,connection)
failure_mode_graph_generator(sample_hyb_name,sample_hyb_failures,connection,"Sample Hybridization Failure Modes")
failure_mode_graph_generator(extension_name,extension_failures,connection,"Extension Failure Modes")
failure_mode_graph_generator(process_failure_name, process_failure_failures, connection,"Total Process Failure Distribution")


seven_day_count = 0
for row in seven_day_completions:
	seven_day_count+=1

print("Over the past seven days " + str(seven_day_count)+ " flowcells have been completed")

one_day_count = 0
for row in one_day_completions:
	one_day_count +=1

print("Yesterday, there was " + str(one_day_count) + " flowcell|s completed")