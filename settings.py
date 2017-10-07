# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:21:03 2017

@author: Joaquin
"""

DOMAIN =\
    { "post":
        { "schema": 
            { # scraped fields
             "date_accessed": {"type":"datetime"}
            , "date_listed": {"type":"datetime"}
            , "description": {}
            , "keyword_tags": {}
            , "post_geolocation": { "type": "string" }
            , "reported_animal" : {"type": "string"}
            , "reported_how": {}
            , "reported_where": {}
            , "source": {"type":"string",
                         "allowed": 
                             [ "Ebay"
                              , "Gumtree"
                              , "Twitter"
                              ]
                        }
            
            , "price": {}
            , "quantity": {}
            , "species": {}
            , "title": { "type": "string" }
            , "unit": {} #kg, individuals, etc.
            , "url": {}
            , "username": {}
            , "uuid": {"type": "string"
                       "unique": True}
              # user - entered fields
            , "additional_notes": {}
            , "case_handler_contact_info": {}
            , "class": {}
            , "common_names": {}
            , "exporter_country": {}
            , "family": {}
            , "genus": {}
            , "importer_country": {}
            , "listing_type": {"type": "string",
                               "allowed": 
                                   [ "Import request"
                                   , "Export offer"
                                   , "Commision"
                                   ] 
                               }
                               
            , "order": {} #taxonomy order
            , "purpose": {} #Trophy, medicine, taxidermy
            , "relevant_authorities": {}
            , "taxon": {}
            , "trader": {} #person
            , "verified by": {} #e.g. sergio.
            }
        }
    }

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']