# portaldev.sph.umich.edu

This is the production (and development) server for the locuszoom API. It hosts a number of services that are required for the API to function. 

## Flask

There are three flask servers running in total: 

1. Production LZ API
2. Development LZ API
3. UKBB API

### Production

### Development

### UKBB

## PostgreSQL 

There are 3 PostgreSQL servers running on the machine. 

1. A version 9.4 server that hosts the production (`api_public_prod`) and staging databases (`api_internal_dev`) for the locuszoom API. 
2. A version 9.5 server that was automatically installed when upgrading to Ubuntu 16.04 LTS. It does not serve anything currently. 
2. A version 10.5 server that hosts the database for the UKBB API. 

## Raw datasets

All of the raw data (with the exception of UKBB) for loading the database also exists on portaldev under `/data/portal_datasets`. 

## LD Server

## Redis

## Jenkins

## Monitor
