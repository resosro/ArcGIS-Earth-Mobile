from __future__ import print_function
import sys
import os.path
import shutil
import json
import datetime
from io import open


#-- Main program
def main(pc_build, pc_header_file, pc_results_file, pc_xml_file, pc_output_file, pc_comments=None):
    #-- Store path to script files
    lc_script_path = os.path.abspath(__file__)
    lc_script_path = lc_script_path.replace("\\", "/")
    lc_script_path = lc_script_path[:lc_script_path.rfind("/") + 1]
    print(" ")
    print("Script Path: " + lc_script_path)

    #-- Check that header file, results file and XML template are accessible
    if not os.path.isfile(pc_header_file):
        if not os.path.isfile(lc_script_path + pc_header_file):
            print("Header file " + pc_header_file + " not found.")
            return 1

    if not os.path.isfile(pc_results_file):
        if not os.path.isfile(lc_script_path + pc_results_file):
            print("Results file " + pc_results_file + " not found.")
            return 1

    if not os.path.isfile(pc_xml_file):
        if not os.path.isfile(lc_script_path + pc_xml_file):
            print("XML Template file " + pc_xml_file + " not found.")
            return 1

    #-- Open header file and grab data
    with open(pc_header_file) as lo_json_file:
        lo_json_data = lo_json_file.read()
        print(" ")
        print("Header file:")
        print(lo_json_data)
        la_header_data = json.loads(lo_json_data)

    #-- Open XML File
    la_xml_file_data=open(pc_xml_file).readlines()

    #-- Replace XML header info
    for ln_lineno in range(0, len(la_xml_file_data)):
        if "<Build></Build>" in la_xml_file_data[ln_lineno]:
            la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<Build></Build>", "<Build>" + pc_build + "</Build>")

        if "<DateTime></DateTime>" in la_xml_file_data[ln_lineno]:
            la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<DateTime></DateTime>", "<DateTime>" + datetime.datetime.now().strftime('%m/%d/%Y %H:%M') + "</DateTime>")

        if "<Email></Email>" in la_xml_file_data[ln_lineno] and "email" in la_header_data.keys():
            la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<Email></Email>", "<Email>" + la_header_data["email"] + "</Email>")

        if "<Platform></Platform>" in la_xml_file_data[ln_lineno] and "platform" in la_header_data.keys():
            la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<Platform></Platform>", "<Platform>" + la_header_data["platform"] + "</Platform>")

        if "<MachineName></MachineName>" in la_xml_file_data[ln_lineno] and "machinename" in la_header_data.keys():
            la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<MachineName></MachineName>", "<MachineName>" + la_header_data["machinename"] + "</MachineName>")

        if "<Owner></Owner>" in la_xml_file_data[ln_lineno] and "owner" in la_header_data.keys():
            la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<Owner></Owner>", "<Owner>" + la_header_data["owner"] + "</Owner>")

        if "<Notes></Notes>" in la_xml_file_data[ln_lineno] and "notes" in la_header_data.keys():
            if la_header_data["notes"] is not None and len(la_header_data["notes"]) > 1:
                la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<Notes></Notes>", "<Notes><![CDATA[" + la_header_data["notes"] + "]]></Notes>")

        if "<TestSuiteComments></TestSuiteComments>" in la_xml_file_data[ln_lineno]:
            if pc_comments:
                la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<TestSuiteComments></TestSuiteComments>", "<TestSuiteComments><![CDATA[" + pc_comments + "]]></TestSuiteComments>")
            elif "testsuitecomments" in la_header_data.keys():
                if la_header_data["testsuitecomments"] is not None and len(la_header_data["testsuitecomments"]) > 1:
                    la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<TestSuiteComments></TestSuiteComments>", "<TestSuiteComments><![CDATA[" + la_header_data["testsuitecomments"] + "]]></TestSuiteComments>")

    #-- Open results file and loop through results
    with open(pc_results_file) as lo_json_file:
        lo_json_data = lo_json_file.read()
        print(" ")
        print("Results file:")
        print(lo_json_data)
        la_results_data = json.loads(lo_json_data)

    for lc_key, la_data in la_results_data.items():
        print("Locating test in XML file: " + lc_key)

        for ln_lineno in range(0, len(la_xml_file_data)):
            try:
                if lc_key.upper() == "UPDATE METRO" or lc_key.upper() == "UPDATE DAILY SHARE":
                    if "<DailyShareUpdated></DailyShareUpdated>" in la_xml_file_data[ln_lineno]:
                      if la_data["results"].upper() == "PASS":
                        la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<DailyShareUpdated></DailyShareUpdated>", "<DailyShareUpdated>yes</DailyShareUpdated>")
                      else:
                        la_xml_file_data[ln_lineno] = la_xml_file_data[ln_lineno].replace("<DailyShareUpdated></DailyShareUpdated>", "<DailyShareUpdated>no</DailyShareUpdated>")
                      
                if lc_key + "\"" in la_xml_file_data[ln_lineno]:
                    print(la_xml_file_data[ln_lineno])
                    ln_temp_lineno = ln_lineno + 1
                    while ln_temp_lineno < len(la_xml_file_data) and "<TestCase" not in la_xml_file_data[ln_temp_lineno]:
                        if "<Result" in la_xml_file_data[ln_temp_lineno]:
                            lc_result = la_xml_file_data[ln_temp_lineno]
                            lc_result = lc_result[:lc_result.find(">")+1] + la_data["results"] + "</Result> \n"
                            la_xml_file_data[ln_temp_lineno] = lc_result

                        if "<Comments>" in la_xml_file_data[ln_temp_lineno]:
                            if la_data["comment"] is not None and len(la_data["comment"]) > 1:
                                la_xml_file_data[ln_temp_lineno] = la_xml_file_data[ln_temp_lineno].replace("<Comments></Comments>", "<Comments><![CDATA[" + la_data["comment"][0:1900] + "]]></Comments>")

                        if "<ImageNameTC>" in la_xml_file_data[ln_temp_lineno] and "image" in la_data.keys():
                            la_xml_file_data[ln_temp_lineno] = la_xml_file_data[ln_temp_lineno].replace("<ImageNameTC></ImageNameTC>", "<ImageNameTC>" + la_data["image"] + "</ImageNameTC>")
                        
                        ln_temp_lineno = ln_temp_lineno + 1
            except:
                continue

    lo_output_file = open(pc_output_file, "w")
    lo_output_file.writelines(la_xml_file_data)
    lo_output_file.close()
    return 0


#-- Call Main program
if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("%s:  Error: %s\n" % (sys.argv[0], "Incorrect number of command options given"))
        print(r"Argument 1 (required): Build (e.g. 8201)")
        print(r"Argument 2 (required): Test header file (e.g. C:\Box Sync\CB_tools\AWS_Scripts\cb_106_sanity_header.json)")
        print(r"Argument 3 (required): Results file (e.g. C:\Box Sync\CB_tools\AWS_Scripts\cb_106_daily_report.json)")
        print(r"Argument 4 (required): XML Template file (e.g. C:\Box Sync\CB_tools\AWS_Scripts\cb_106_sanity_results.xml)")
        print(r"Argument 5 (required): Output XML file (e.g. C:\Box Sync\CB_tools\AWS_Scripts\cb_106_sanity_results_8201.xml)")
        print(r"Argument 6 (optional): Comments (e.g. Build sanity failed due to XYZ)")
        print(" ")
        sys.exit(3)
    else:
        pc_build = sys.argv[1]
        pc_header_file = sys.argv[2]
        pc_results_file = sys.argv[3]
        pc_xml_file = sys.argv[4]
        pc_output_file = sys.argv[5]

        if len(sys.argv) > 6:
            pc_comments = sys.argv[6]
        else:
            pc_comments = ""

    ln_exit_code = main(pc_build, pc_header_file, pc_results_file, pc_xml_file, pc_output_file, pc_comments)
    sys.exit(ln_exit_code)