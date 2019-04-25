PGDMP     /                     w            e_accounting    10.7    10.7     	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    25106    e_accounting    DATABASE     �   CREATE DATABASE e_accounting WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United Kingdom.1252' LC_CTYPE = 'English_United Kingdom.1252';
    DROP DATABASE e_accounting;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false                       0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    25128    barang    TABLE     	  CREATE TABLE public.barang (
    id integer NOT NULL,
    name character varying NOT NULL,
    jumlah integer,
    hb double precision,
    hj double precision,
    created_at timestamp without time zone,
    status_enabled boolean,
    satuan character varying
);
    DROP TABLE public.barang;
       public         postgres    false    3            �            1259    25126    barang_id_seq    SEQUENCE     �   CREATE SEQUENCE public.barang_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.barang_id_seq;
       public       postgres    false    201    3                       0    0    barang_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.barang_id_seq OWNED BY public.barang.id;
            public       postgres    false    200            �            1259    25109    cashflow    TABLE       CREATE TABLE public.cashflow (
    id integer NOT NULL,
    created_at timestamp without time zone,
    status_enabled boolean,
    cash_in double precision,
    cash_out double precision,
    balance double precision,
    id_transaksi integer,
    keterangan character varying
);
    DROP TABLE public.cashflow;
       public         postgres    false    3            �            1259    25107    cashflow_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cashflow_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.cashflow_id_seq;
       public       postgres    false    197    3                       0    0    cashflow_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.cashflow_id_seq OWNED BY public.cashflow.id;
            public       postgres    false    196            �            1259    25117 	   transaksi    TABLE     �   CREATE TABLE public.transaksi (
    id integer NOT NULL,
    name character varying NOT NULL,
    created_at timestamp without time zone,
    status_enabled boolean,
    id_barang integer,
    jumlah integer,
    tipe character varying
);
    DROP TABLE public.transaksi;
       public         postgres    false    3            �            1259    25115    transaksi_id_seq    SEQUENCE     �   CREATE SEQUENCE public.transaksi_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.transaksi_id_seq;
       public       postgres    false    199    3                       0    0    transaksi_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.transaksi_id_seq OWNED BY public.transaksi.id;
            public       postgres    false    198            
           2604    25131 	   barang id    DEFAULT     f   ALTER TABLE ONLY public.barang ALTER COLUMN id SET DEFAULT nextval('public.barang_id_seq'::regclass);
 8   ALTER TABLE public.barang ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    200    201    201            }
           2604    25112    cashflow id    DEFAULT     j   ALTER TABLE ONLY public.cashflow ALTER COLUMN id SET DEFAULT nextval('public.cashflow_id_seq'::regclass);
 :   ALTER TABLE public.cashflow ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    196    197    197            ~
           2604    25120    transaksi id    DEFAULT     l   ALTER TABLE ONLY public.transaksi ALTER COLUMN id SET DEFAULT nextval('public.transaksi_id_seq'::regclass);
 ;   ALTER TABLE public.transaksi ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    199    198    199                      0    25128    barang 
   TABLE DATA               ^   COPY public.barang (id, name, jumlah, hb, hj, created_at, status_enabled, satuan) FROM stdin;
    public       postgres    false    201   �                  0    25109    cashflow 
   TABLE DATA               x   COPY public.cashflow (id, created_at, status_enabled, cash_in, cash_out, balance, id_transaksi, keterangan) FROM stdin;
    public       postgres    false    197   z!                 0    25117 	   transaksi 
   TABLE DATA               b   COPY public.transaksi (id, name, created_at, status_enabled, id_barang, jumlah, tipe) FROM stdin;
    public       postgres    false    199   �"                  0    0    barang_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.barang_id_seq', 5, true);
            public       postgres    false    200                       0    0    cashflow_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.cashflow_id_seq', 18, true);
            public       postgres    false    196                       0    0    transaksi_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.transaksi_id_seq', 24, true);
            public       postgres    false    198            �
           2606    25136    barang barang_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.barang
    ADD CONSTRAINT barang_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.barang DROP CONSTRAINT barang_pkey;
       public         postgres    false    201            �
           2606    25114    cashflow cashflow_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.cashflow
    ADD CONSTRAINT cashflow_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.cashflow DROP CONSTRAINT cashflow_pkey;
       public         postgres    false    197            �
           2606    25125    transaksi transaksi_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.transaksi DROP CONSTRAINT transaksi_pkey;
       public         postgres    false    199            �
           2606    25150 #   cashflow cashflow_id_transaksi_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cashflow
    ADD CONSTRAINT cashflow_id_transaksi_fkey FOREIGN KEY (id_transaksi) REFERENCES public.transaksi(id);
 M   ALTER TABLE ONLY public.cashflow DROP CONSTRAINT cashflow_id_transaksi_fkey;
       public       postgres    false    197    199    2691            �
           2606    25137 "   transaksi transaksi_id_barang_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_id_barang_fkey FOREIGN KEY (id_barang) REFERENCES public.barang(id);
 L   ALTER TABLE ONLY public.transaksi DROP CONSTRAINT transaksi_id_barang_fkey;
       public       postgres    false    201    199    2693               �   x���I�0E��)� ���g�&�P�@)��-uտ������:�n��X����#�MOؑMLI�6���`}%�K� 0�@�H�8�h�k�*|v-�׼`���cK�c�%/Oeaʯ��@���2^]N��$C	�&��ܾ�i��n=           x���KN�0�}
_��<;ξ���C�Z)q}�hTP��7�O��xA��愠�jv�p]� �+�F,��n��S�]��U"T�HX�vo�j�qP�z]ղ�ì����� h�-Z�1ߌA�*�wL}����r�Vמ���`a|��e�5�_aQ/g�u��T�����>��?'��k�R)aF�h���4d��h�G�1�D�[��c�uO����FdOTb�*F�4lE	e�#^�}���F4~�i�H=[�����h9�y         �   x���An�@е9�/���1�}{�nLA)M$��7����r$���g��x��ʾ���N,� ��tǄ�G���N��C&����8��2�X���صN*o!ߣu�7��DNK�6��eG"���(�2��b��Z���U6D��W��C�����)�֦�U������v�P�E��^©�߽����+�G;�#饸H�})Sw9��b�i|Y��۪�e�Rۡ_     