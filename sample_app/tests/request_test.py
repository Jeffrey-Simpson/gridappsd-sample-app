import json
import time
import os
import argparse
import goss_forward_sim
from gridappsd import GOSS

goss_sim = "goss.gridappsd.process.request.simulation"
test_topic = 'goss.gridappsd.test'
responseQueueTopic = '/temp-queue/response-queue'
goss_simulation_status_topic = '/topic/goss.gridappsd/simulation/status/'


def _startTest(username,password,gossServer='localhost',stompPort='61613', simulationID=1234, rulePort=5000, topic="input"):
    loc = os.path.realpath(__file__)
    loc =  os.path.dirname(loc)
    # loc =  os.path.dirname(os.path.dirname(os.path.dirname(loc)))
    loc ='/gridappsd/applications/sample_app/tests' # DOCKER
    print (loc)
    testCfg = {"testConfigPath":loc+"/SampleTestConfig.json",
            "testScriptPath":loc+"/SampleTestScript.json",
            "simulationID": 1234,
            "rulePort": 5000,
            "topic":"input",
            "expectedResult":loc + "/expected_result_series_filtered_8500.json"
            }

    simCfg=''' {\"power_system_config\":{\"SubGeographicalRegion_name\":\"_1CD7D2EE-3C91-3248-5662-A43EFEFAC224\",\"GeographicalRegion_name\":\"_24809814-4EC6-29D2-B509-7F8BFB646437\",\"Line_name\":\"_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3\"},\"simulation_config\":{\"power_flow_solver_method\":\"NR\",\"duration\":120,\"simulation_name\":\"ieee8500\",\"simulator\":\"GridLAB-D\",\"start_time\":\"2009-07-21 00:00:00\",\"timestep_frequency\":1000,\"timestep_increment\":1000,\"simulation_output\":{\"output_objects\":[{\"name\":\"rcon_FEEDER_REG\",\"properties\":[\"connect_type\",\"Control\",\"control_level\",\"PT_phase\",\"band_center\",\"band_width\",\"dwell_time\",\"raise_taps\",\"lower_taps\",\"regulation\"]},{\"name\":\"rcon_VREG2\",\"properties\":[\"connect_type\",\"Control\",\"control_level\",\"PT_phase\",\"band_center\",\"band_width\",\"dwell_time\",\"raise_taps\",\"lower_taps\",\"regulation\"]},{\"name\":\"rcon_VREG3\",\"properties\":[\"connect_type\",\"Control\",\"control_level\",\"PT_phase\",\"band_center\",\"band_width\",\"dwell_time\",\"raise_taps\",\"lower_taps\",\"regulation\"]},{\"name\":\"rcon_VREG4\",\"properties\":[\"connect_type\",\"Control\",\"control_level\",\"PT_phase\",\"band_center\",\"band_width\",\"dwell_time\",\"raise_taps\",\"lower_taps\",\"regulation\"]},{\"name\":\"reg_FEEDER_REG\",\"properties\":[\"configuration\",\"phases\",\"to\",\"tap_A\",\"tap_B\",\"tap_C\"]},{\"name\":\"reg_VREG2\",\"properties\":[\"configuration\",\"phases\",\"to\",\"tap_A\",\"tap_B\",\"tap_C\"]},{\"name\":\"reg_VREG3\",\"properties\":[\"configuration\",\"phases\",\"to\",\"tap_A\",\"tap_B\",\"tap_C\"]},{\"name\":\"reg_VREG4\",\"properties\":[\"configuration\",\"phases\",\"to\",\"tap_A\",\"tap_B\",\"tap_C\"]},{\"name\":\"cap_capbank0a\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_A\",\"dwell_time\",\"switchA\"]},{\"name\":\"cap_capbank1a\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_A\",\"dwell_time\",\"switchA\"]},{\"name\":\"cap_capbank2a\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_A\",\"dwell_time\",\"switchA\"]},{\"name\":\"cap_capbank0b\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_B\",\"dwell_time\",\"switchB\"]},{\"name\":\"cap_capbank1b\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_B\",\"dwell_time\",\"switchB\"]},{\"name\":\"cap_capbank2b\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_B\",\"dwell_time\",\"switchB\"]},{\"name\":\"cap_capbank0c\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_C\",\"dwell_time\",\"switchC\"]},{\"name\":\"cap_capbank1c\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_C\",\"dwell_time\",\"switchC\"]},{\"name\":\"cap_capbank2c\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_C\",\"dwell_time\",\"switchC\"]},{\"name\":\"cap_capbank3\",\"properties\":[\"phases\",\"pt_phase\",\"phases_connected\",\"control\",\"control_level\",\"capacitor_A\",\"capacitor_B\",\"capacitor_C\",\"dwell_time\",\"switchA\",\"switchB\",\"switchC\"]},{\"name\":\"xf_hvmv_sub\",\"properties\":[\"power_in_A\",\"power_in_B\",\"power_in_C\"]},{\"name\":\"l2955047\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"l2673313\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"l3160107\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"l2876814\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"l3254238\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"m1047574\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"_hvmv_sub_lsb\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"190-8593\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"190-8581\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]},{\"name\":\"190-7361\",\"properties\":[\"voltage_A\",\"voltage_B\",\"voltage_C\"]}]},\"model_creation_config\":{\"load_scaling_factor\":1.0,\"triplex\":\"y\",\"encoding\":\"u\",\"system_frequency\":60,\"voltage_multiplier\":1.0,\"power_unit_conversion\":1.0,\"unique_names\":\"y\",\"schedule_name\":\"ieeezipload\",\"z_fraction\":0.0,\"i_fraction\":1.0,\"p_fraction\":0.0},\"simulation_broker_port\":5570,\"simulation_broker_location\":\"127.0.0.1\"},\"application_config\":{\"applications\":[{\"name\":\"sample_app\",\"config_string\":\"\"}]}}'''

    goss = GOSS()
    goss.connect()

    # simulationId =123
    simulationId = goss.get_response(goss_sim, simCfg)
    print('sent simulation request')
    time.sleep(1)
    testCfg['simulationID']=simulationId
    testCfg = json.dumps(testCfg)
    print(testCfg)
    goss.send(test_topic, testCfg)

    time.sleep(1)
    print('sent test request')

    # goss_forward_sim.forward_sim_ouput(str(simulationId))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--topic", type=str, help="topic, the default is input", default="input", required=False)
    parser.add_argument("-p","--port", type=int, help="port number, the default is 5000", default=5000, required=False)
    parser.add_argument("-i", "--id", type=int, help="simulation id", required=False)
    # parser.add_argument("--start_date", type=str, help="Simulation start date", default="2017-07-21 12:00:00", required=False)
    # parser.add_argument("--end_date", type=str, help="Simulation end date" , default="2017-07-22 12:00:00", required=False)
    # parser.add_argument('-o', '--options', type=str, default='{}')
    args = parser.parse_args()

    _startTest('system','manager',gossServer='127.0.0.1',stompPort='61613', simulationID=args.id, rulePort=args.port, topic=args.topic)
