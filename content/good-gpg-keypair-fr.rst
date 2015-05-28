:Title: Créer une bonne clef GPG
:Date: 2015-05-26 23:14
:Category: Bonnes pratiques
:Status: draft
:Slug: gpg-good-keypair
:Lang: fr

Créer sa clef pour signer
-------------------------

.. code-block:: bash
   
   gpg --gen-key

* RSA (signature seule)
* 4096
* 0 n'expire jamais

Créer ses sous-clefs
--------------------

.. code-block:: bash
   
   gpg --list-keys [IDENTIFIANT-CLEF]
   gpg --edit-key [IDENTIFIANT-CLEF]

* addkey
* RSA (sign only)
* 4096
* Choose an expiry date

* addkey
* RSA (chiffrement seul)
* 4096
* Choose an expiry date

* save

Améliorer les options par défaut
--------------------------------

.. code-block:: bash

   gpg --edit-key [IDENTIFIANT-CLEF]

* setpref SHA512 SHA384 SHA256 SHA224 AES256 AES192 AES CAST5 ZLIB
  BZIP2 ZIP Uncompressed
* save

Sauvegarde
----------

.. code-block:: bash
   
   umask 077; tar -cf $HOME/gnupg-backup.tar -C $HOME .gnupg


Retirer la clef privée maitre du trousseau
------------------------------------------

.. code-block:: bash

   gpg --export-secret-subkeys [IDENTIFIANT-CLEF] > secret-subkeys
   gpg --delete-secret-key [IDENTIFIANT-CLEF]
   gpg --import secret-subkeys
   shred shred -n 5 -u secret-subkeys

* gpg -K montre "sec#" à la place de "sec".

.. code-block:: bash

   gpg --edit-key [IDENTIFIANT-CLEF]

* passwd
* save

Si la clef maitre est nécessaire
--------------------------------

.. code-block:: bash

   gpg --homedir=/chemin/vers/sauvegarde -K

or

.. code-block:: bash

   export GNUPGHOME=/chemin/vers/sauvegarde
   gpg -K

Revocation
----------

.. code-block:: bash

   gpg --gen-revoke --armor [IDENTIFIANT-CLEF] > $HOME/[IDENTIFIANT-CLEF]-revoke.gpg
   gpg --export-secret-keys --armor [IDENTIFIANT-CLEF] > $HOME/[IDENTIFIANT-CLEF]-private.gpg
   gpg --export --armor [IDENTIFIANT-CLEF] > $HOME/[IDENTIFIANT-CLEF]-public.gpg

.. code-block:: bash

   export GNUPGHOME=/chemin/vers/sauvegarde
   gpg --edit-key [IDENTIFIANT-CLEF]

* list
* key [NUMERO]
* revkey
* save

Envoyer la clef sur les serveurs de clefs

* https://gaffer.ptitcanardnoir.org/intrigeri/code/parcimonie/

* https://wiki.debian.org/Subkeys?action=show&redirect=subkeys
* https://wiki.debian.org/Keysigning
* http://keyring.debian.org/creating-key.html
* https://alexcabal.com/creating-the-perfect-gpg-keypair/
