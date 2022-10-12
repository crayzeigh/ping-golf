# Ping Golf

Created for Equinix as a simple booth demo/game to encourage engagement with the platform in exchange for giveaways

## Quickstart

To run ping golf, clone this repository and run `make URL="$YourDbUrl"` replacing `$YourDbUrl` 
with the appropriate `postgresql://` URL for connecting to your database. 

## Function

The `web.py` script has three main functions. A small testing/placeholder site at `/`, a way to generate and 
ingest players' user agent and ping times using the `POST` method on `/`, and a Highscores page to display 
ping times and user agent entries in ascending order of ping at `/scorebaord`.

## Database URL

You'll need to supply the proper postgresql connection URL as an arguement to `make` or edit the `makefile` 
to include your specific connection URL for it to work. Alternately, you can `export DATABASE_URL` with the 
appropriate value and run `web.py` manually, without usingthe `makefile`. 