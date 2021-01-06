# jitsi2prometheus

This repository has been created for jitsi + prometheus docker environments.

![Img](./jitsi2prometheus2grafana.png)

* Enable Jitsi Statistics on port 8080 in the `.env` file of your dockerized jitsi instance.
  ```
  JVB_ENABLE_APIS=rest,colibri
  ```

* `prometheus.yml`
  ```
  - job_name: 'jitsi'
    static_configs:
    - targets: ['jitsi2prometheus:8080']
  ```
