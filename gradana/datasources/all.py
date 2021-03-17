# https://github.com/cirocosta/sample-grafana/blob/master/grafana/provisioning/dashboards/all.yml

datasources:
-  access: 'proxy'                       # make grafana perform the requests
   editable: true                        # whether it should be editable
   is_default: true                      # whether this should be the default DS
   name: 'k8s'                           # name of the datasource
   org_id: 1                             # id of the organization to tie this datasource to
   type: 'prometheus'                    # type of the data source
   url: 'http://k8s-prom.vbox.priv'      # url of the prom instance
   version: 1                            # well, versioning
