# Send Image Client

This example demonstrates how to send an image to Kaa.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Like all other examples, this one requires **environment variables** to interact with the Kaa API. The most commonly required variables are:

-   `DEFAULT_KPC_HOST`
-   `APPLICATION_VERSION`
-   `ENDPOINT_TOKEN`

Here’s how to obtain them:

-   **`APPLICATION_VERSION`**: Look [here](https://www.kaaiot.com/docs/terms-and-concepts#application-version).
-   **`ENDPOINT_TOKEN`**: Look [here](https://www.kaaiot.com/docs/terms-and-concepts#endpoint-token).
-   **`DEFAULT_KPC_HOST`**: This is either `mqtt.next.kaaiot.com` or `mqtt.cloud.kaaiot.com`, depending on which version of the Kaa platform you're using.

## Provisioning Your Python Script

Here's an example of the credentials you should provide. Replace the placeholder values with your own and copy the result into your terminal:

```bash
export DEFAULT_KPC_HOST="{your-kaa-kpc-host}"
export DEFAULT_KPC_PORT="1883"
export APPLICATION_VERSION="{your-application-version}"
export ENDPOINT_TOKEN="{your-endpoint-token}"
```

Alternatively, you can add the same values to a .env file:

```bash
DEFAULT_KPC_HOST="{your-kaa-kpc-host}"
DEFAULT_KPC_PORT="1883"
APPLICATION_VERSION="{your-application-version}"
ENDPOINT_TOKEN="{your-endpoint-token}"
```

## Run the Script

```
python3 main.py
```
