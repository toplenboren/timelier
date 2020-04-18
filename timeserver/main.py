import timeserver
import timegetter
import utils

if __name__ == "__main__":
    yml = utils.read_yaml_into_dict('configuration.yml')
    dependencies = {
        'timegetter': timegetter.get_time_from_os
    }

    configuration = dict(yml, **dependencies)

    timeserver.start(configuration)
