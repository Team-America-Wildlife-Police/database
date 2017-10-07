# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:21:03 2017

@author: Joaquin
"""

DOMAIN =\
    { "posts":
        { "schema": 
            { "title": { "type": "string" }
            , "username": { "type": "string" }
            , "uuid": {"type":"string"}
            , "source": { "type": "string" }
            , "url": {"type":"string"}
            , "date": {"type":"datetime"}
            , "location": { "type": "string" }
            , "description": {}
            , "price": {}
            }
        }
    , "accounts": 
        { "schema": 
            { "site": { "type": "string" }
            , "username": { "type": "string" }
            }
        }
    , "traders": 
        { "schema": 
            { "accounts": 
                { "type": "list"
                , "schema": 
                    { "type": "objectid"
                    , "data_relation": 
                        { "resource": "accounts"
                        , "field": "_id"
                        , "embeddable": True
                        }
                    }
                }
            }
        }
    , "taxon":
        { "schema":
            { 
            , 
             }
        }
    }
}