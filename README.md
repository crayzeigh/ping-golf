# Ping Golf

Created for Equinix as a simple booth demo/game to encourage engagement with the platform in exchange for giveaways

## Quickstart

To run ping golf, clone this repository and run `make URL="$YourDbUrl"` replacing `$YourDbUrl` 
with the appropriate `postgresql://` URL for connecting to your database. This may generate some errors (see the Bird section below) but should still run the application. 

To run ping golf if you've got bird install to handle BGP advertisement, run `make URL="$yourDbUrl" ANYCAST_IP="any.cast.ip.address"`

## Function

The `web.py` script has three main functions. A small testing/placeholder site at `/`, a way to generate and 
ingest players' user agent and ping times using the `POST` method on `/`, and a Highscores page to display 
ping times and user agent entries in ascending order of ping at `/scorebaord`.

## Database URL

You'll need to supply the proper postgresql connection URL as an arguement to `make` or edit the `makefile` 
to include your specific connection URL for it to work. Alternately, you can `export DATABASE_URL` with the 
appropriate value and run `web.py` manually, without usingthe `makefile`. 

## Bird

This version has the addition of using the bird service to advertise an anycast IP address to your BPG peers. I haven't cleaned it to turn this off without manually editing the makefile to exclude it. To enable you'll want to pass your anycast ip along with the initial `make` or `make bird` commands. You can also drop a dummy file in `/etc/bird/bird.conf` which will cause make to skip creating this file and restarting the service. If you don't either specify `ANYCAST_IP="some.ip.add.ress"` or create a dummy file, you're likely to get errors relating to bird while the app still runs.